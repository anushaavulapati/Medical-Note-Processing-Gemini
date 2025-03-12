import pandas as pd

from bert import similarity
from variables import admission_attributes, delivery_attributes, example_note2, example_format2, example_note, example_format, example_format_delivery, example_format_admission

def retrieve_encounter_admission_info(notes,encounter_id,model):
    #Read ground truth for note titles from user input. Training data contains manually labeled note titles.
    admissionnote_train_df = pd.read_csv('admissionvalidity_train.csv')

    for note in notes:
        #Check if input note is a valid admission note or not, leveraging similarity search.
        #Validity depends on whether note title is most similar to a valid admission note or an invalid note title from training data
        valid = similarity(note[1], admissionnote_train_df)
        if valid[1] == 'valid':
        #If note is a valid admission note, query Gemini API for attribute information in admission note
            query = "attributes: " + ", ".join(admission_attributes) + " /n " + example_note2 + " /n " + "example format: " + "/n" + example_format_admission.replace("/n", "<br/>")  + " /n " + "Given the above example note and format /n" + " From the following note, for all attributes in the above attribute list compulsorily return attribute and value along with sentence containing relevant attribute information in csv format with commas and each attribute having its own row." + "/n" + note[0]
            response = model.generate_content(query)

            #Store attribute information in CSV
            data = response.parts[0].text
            csv_name = "adm_" + str(encounter_id) + note[1]
            csv_name = "".join(char for char in csv_name if char.isalnum())
            csv_name += ".csv"
            data = [line.split(',', maxsplit=2) for line in data.splitlines()]
            df = pd.DataFrame(data=data)
            print(csv_name)
            df.to_csv(csv_name, index=False)
            return True
    return False

def retrieve_encounter_antepartum_info(notes,encounter_id,model):
    for note in notes:
        query = "attributes: " + ", ".join(
            admission_attributes) + " /n " + example_note2 + " /n " + "example format: " + "/n" + example_format_admission + " /n " + "Given the above example note and format /n" + " From the following note, for all attributes in the above attribute list compulsorily return attribute and value along with sentence containing relevant attribute information in csv format with commas and each attribute having its own row." + "/n" + \
                note[0]
        response = model.generate_content(query)

        data = response.parts[0].text
        csv_name = "adm_" + str(encounter_id) + note[1]
        csv_name = "".join(char for char in csv_name if char.isalnum())
        csv_name += ".csv"
        data = [line.split(',', maxsplit=2) for line in data.splitlines()]
        df = pd.DataFrame(data=data)
        print(csv_name)
        df.to_csv(csv_name, index=False)
        return True
    return False

def retrieve_encounter_delivery_info(notes,encounter_id,model):
    #Read ground truth for note titles from user input. Training data contains manually labeled note titles.
    deliverynote_train_df = pd.read_csv('deliveryvalidity_train.csv')

    for note in notes:
        #Check if input note is a valid delivery note or not, leveraging similarity search.
        #Validity depends on whether note title is most similar to a valid delivery/discharge note title or an invalid note title from training data
        valid = similarity(note[1], deliverynote_train_df)
        if valid[1] == 'valid':
            #If note is a valid delivery/discharge note, query Gemini API for attribute information in delivery/discharge note
            query = "attributes: " + ", ".join(delivery_attributes) + " /n " + example_note2 + " /n " + "example format: " + "/n" + example_format_delivery.replace("/n", "<br/>") + " /n " + "Given the above example note and format /n" + " From the following note, for all attributes in the above attribute list compulsorily return attribute and value along with sentence containing relevant attribute information in csv format with commas and each attribute having its own row." + "/n" + note[0]
            response = model.generate_content(query)

            #Store attribute information in CSV
            data = response.parts[0].text
            csv_name = "dlv_" + str(encounter_id) + note[1]
            csv_name = "".join(char for char in csv_name if char.isalnum())
            csv_name += ".csv"
            data = [line.split(',', maxsplit=2) for line in data.splitlines()]
            df = pd.DataFrame(data=data)
            print(csv_name)
            df.to_csv(csv_name, index=False)
            return True
    return False