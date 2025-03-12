from db import create_connection,retrieve_admission_note, retrieve_delivery_note, retrieve_antepartuminformation_note
from gemini import retrieve_encounter_admission_info, retrieve_encounter_antepartum_info, retrieve_encounter_delivery_info

GOOGLE_API_KEY = ''
import google.generativeai as genai
#Configuring genai to pickup our api key
genai.configure(api_key=GOOGLE_API_KEY)


def main():
    #Connecting to database
    connection = create_connection()

    #Taking user input for mother id, encounter id and attribute
    encounter_id = input("Enter encounter id:")

    #If connection is successful, send query to Gemini to search note for attribute
    if connection:
        #Initalize gemini model
        model = genai.GenerativeModel('gemini-pro')

        # Retrieve possible delivery notes from database
        delivery_notes = retrieve_delivery_note(connection, encounter_id)
        # Extract attribute values at delivery time
        retrieve_encounter_delivery_info(delivery_notes, encounter_id, model)

        #Retrieve possible admission notes from database
        admission_notes = retrieve_admission_note(connection, encounter_id)
        admission_info_extracted = retrieve_encounter_admission_info(admission_notes, encounter_id, model)

        #If admission note not present, retrieve admission attributes from antepartuminformation note instead
        if not admission_info_extracted:
            antepartum_notes = retrieve_antepartuminformation_note(connection, encounter_id)
            retrieve_encounter_antepartum_info(antepartum_notes, encounter_id, model)




main()
