import torch
from tqdm.notebook import tqdm
from transformers import BertTokenizer
from torch.utils.data import TensorDataset
import numpy as np
from transformers import BertForSequenceClassification, AutoModel

def similarity(term,df):
    #Loading model and tokenizer
    model_name = 'bert-base-uncased'
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)

    # Extracting note titles and target note title
    note_titles = df['note_title'].tolist()
    valids = df['valid'].tolist()

    # Encodes note titles and target node title
    target_word_encoded = tokenizer.encode(term, return_tensors='pt').unsqueeze(0)
    word_list_encoded = [tokenizer.encode(word, return_tensors='pt').unsqueeze(0) for word in note_titles]

    # Pad each sequence so they have the same length
    max_len = max(target_word_encoded.shape[1], max(word_encoded.shape[1] for word_encoded in word_list_encoded))
    target_word_encoded = torch.nn.functional.pad(target_word_encoded,
                                                  (0, 0, 0, max_len - target_word_encoded.shape[1]))
    word_list_encoded = [torch.nn.functional.pad(word_encoded, (0, 0, 0, max_len - word_encoded.shape[1])) for
                         word_encoded in word_list_encoded]

    # Calculate the similarities
    with torch.no_grad():
        target_word_encoded = target_word_encoded.squeeze(0)
        #Generate embedding for target note title
        target_word_embedding = torch.mean(model(input_ids=target_word_encoded)['last_hidden_state'][0][1:-1], dim=0)
        similarities = []
        for word_encoded in word_list_encoded:
            word_encoded = word_encoded.squeeze(0)
            word_embedding = torch.mean(model(input_ids=word_encoded)['last_hidden_state'][0][1:-1], dim=0)
            #Calculate similarities between note titles with cosine similarity
            similarity = torch.nn.functional.cosine_similarity(target_word_embedding.reshape(1, -1),
                                                               word_embedding.reshape(1, -1)).item()
            similarities.append(similarity)

    validities = ['invalid','valid']

    # Print the similarities
    return [max(similarities), validities[valids[similarities.index(max(similarities))]], note_titles[similarities.index(max(similarities))], term]

def predict(example):
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                          num_labels=2,
                                                          output_attentions=False,
                                                          output_hidden_states=False)

    model.to(device)

    model.load_state_dict(torch.load('finetuned_BERT_epoch_5.model', map_location=torch.device('cpu')))
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
                                              do_lower_case=True)
    encoded = tokenizer.encode_plus(
        example,
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=100,
        return_tensors='pt'
    )

    input_ids = encoded['input_ids'].to(device)
    attention_mask = encoded['attention_mask'].to(device)

    output = model(input_ids, attention_mask)
    valids = ["valid","invalid"]
    logits = [output.logits[0][0].item(),output.logits[0][1].item()]
    print(example)
    print(output)
    print(valids[logits.index(max(logits))])


def bert(df):
    possible_labels = df.valid.unique()

    label_dict = {}
    for index, possible_label in enumerate(possible_labels):
        label_dict[possible_label] = index

    df['label'] = df.valid.replace(label_dict)

    from sklearn.model_selection import train_test_split

    X_train, X_val, y_train, y_val = train_test_split(df.index.values,
                                                      df.label.values,
                                                      test_size=0.15,
                                                      random_state=42,
                                                      stratify=df.label.values)

    df['data_type'] = ['not_set'] * df.shape[0]

    df.loc[X_train, 'data_type'] = 'train'
    df.loc[X_val, 'data_type'] = 'val'

    df.groupby(['valid', 'label', 'data_type']).count()

    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased',
                                              do_lower_case=True)

    encoded_data_train = tokenizer.batch_encode_plus(
        df[df.data_type == 'train'].note_title.values,
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=100,
        return_tensors='pt'
    )

    encoded_data_val = tokenizer.batch_encode_plus(
        df[df.data_type == 'val'].note_title.values,
        add_special_tokens=True,
        return_attention_mask=True,
        pad_to_max_length=True,
        max_length=100,
        return_tensors='pt'
    )

    input_ids_train = encoded_data_train['input_ids']
    attention_masks_train = encoded_data_train['attention_mask']
    labels_train = torch.tensor(df[df.data_type == 'train'].label.values)

    input_ids_val = encoded_data_val['input_ids']
    attention_masks_val = encoded_data_val['attention_mask']
    labels_val = torch.tensor(df[df.data_type == 'val'].label.values)

    dataset_train = TensorDataset(input_ids_train, attention_masks_train, labels_train)
    dataset_val = TensorDataset(input_ids_val, attention_masks_val, labels_val)

    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                          num_labels=len(label_dict),
                                                          output_attentions=False,
                                                          output_hidden_states=False)

    from torch.utils.data import DataLoader, RandomSampler, SequentialSampler

    batch_size = 3

    dataloader_train = DataLoader(dataset_train,
                                  sampler=RandomSampler(dataset_train),
                                  batch_size=batch_size)

    dataloader_validation = DataLoader(dataset_val,
                                       sampler=SequentialSampler(dataset_val),
                                       batch_size=batch_size)

    from transformers import AdamW, get_linear_schedule_with_warmup

    optimizer = AdamW(model.parameters(),
                      lr=1e-5,
                      eps=1e-8)

    epochs = 5

    scheduler = get_linear_schedule_with_warmup(optimizer,
                                                num_warmup_steps=0,
                                                num_training_steps=len(dataloader_train) * epochs)

    from sklearn.metrics import f1_score

    def f1_score_func(preds, labels):
        preds_flat = np.argmax(preds, axis=1).flatten()
        labels_flat = labels.flatten()
        return f1_score(labels_flat, preds_flat, average='weighted')

    def accuracy_per_class(preds, labels):
        label_dict_inverse = {v: k for k, v in label_dict.items()}

        preds_flat = np.argmax(preds, axis=1).flatten()
        labels_flat = labels.flatten()

        for label in np.unique(labels_flat):
            y_preds = preds_flat[labels_flat == label]
            y_true = labels_flat[labels_flat == label]
            print(f'Class: {label_dict_inverse[label]}')
            print(f'Accuracy: {len(y_preds[y_preds == label])}/{len(y_true)}\n')

    import random

    seed_val = 17
    random.seed(seed_val)
    np.random.seed(seed_val)
    torch.manual_seed(seed_val)
    torch.cuda.manual_seed_all(seed_val)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    def evaluate(dataloader_val):

        model.eval()

        loss_val_total = 0
        predictions, true_vals = [], []

        for batch in dataloader_val:
            batch = tuple(b.to(device) for b in batch)

            inputs = {'input_ids': batch[0],
                      'attention_mask': batch[1],
                      'labels': batch[2],
                      }

            with torch.no_grad():
                outputs = model(**inputs)

            loss = outputs[0]
            logits = outputs[1]
            loss_val_total += loss.item()

            logits = logits.detach().cpu().numpy()
            label_ids = inputs['labels'].cpu().numpy()
            predictions.append(logits)
            true_vals.append(label_ids)

        loss_val_avg = loss_val_total / len(dataloader_val)

        predictions = np.concatenate(predictions, axis=0)
        true_vals = np.concatenate(true_vals, axis=0)

        return loss_val_avg, predictions, true_vals

    for epoch in tqdm(range(1, epochs + 1)):

        model.train()

        loss_train_total = 0

        progress_bar = tqdm(dataloader_train, desc='Epoch {:1d}'.format(epoch), leave=False, disable=False)
        for batch in progress_bar:
            model.zero_grad()

            batch = tuple(b.to(device) for b in batch)

            inputs = {'input_ids': batch[0],
                      'attention_mask': batch[1],
                      'labels': batch[2],
                      }

            outputs = model(**inputs)

            loss = outputs[0]
            loss_train_total += loss.item()
            loss.backward()

            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)

            optimizer.step()
            scheduler.step()

            progress_bar.set_postfix({'training_loss': '{:.3f}'.format(loss.item() / len(batch))})

        torch.save(model.state_dict(), f'finetuned_BERT_epoch_{epoch}.model')

        tqdm.write(f'\nEpoch {epoch}')

        loss_train_avg = loss_train_total / len(dataloader_train)
        tqdm.write(f'Training loss: {loss_train_avg}')

        val_loss, predictions, true_vals = evaluate(dataloader_validation)
        val_f1 = f1_score_func(predictions, true_vals)
        tqdm.write(f'Validation loss: {val_loss}')
        tqdm.write(f'F1 Score (Weighted): {val_f1}')

    model = BertForSequenceClassification.from_pretrained("bert-base-uncased",
                                                          num_labels=len(label_dict),
                                                          output_attentions=False,
                                                          output_hidden_states=False)

    model.to(device)

    model.load_state_dict(torch.load('finetuned_BERT_epoch_1.model', map_location=torch.device('cpu')))

    _, predictions, true_vals = evaluate(dataloader_validation)
    print(accuracy_per_class(predictions, true_vals))
