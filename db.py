import psycopg2

#DB credentials
db_username = "rohan"
db_password = "Rohan123"
db_host = "172.31.158.228"
db_name = "postgres"


#Function to connect to database
def create_connection():
    try:
    #function for connection
        connection = psycopg2.connect(
            user=db_username,
            password=db_password,
            host=db_host,
            database=db_name
        )
        print("Database connected successfully")
        return connection
    except Exception as e:
        print("Error connecting to the database:", str(e))
        raise

#Function to retrieve admission note from the FHR database
def retrieve_admission_note(connection, encounter_id):
    try:
      with connection.cursor() as cursor:
        # SQL query to select note according to mother id and encounter id
        query = f"SELECT note, note_title FROM child_structured_data_2022.mother_notes WHERE mother_encounter_id = {encounter_id} AND (note_title LIKE '%admission%' OR note_title LIKE '%h&p%')"
        cursor.execute(query)
        note = cursor.fetchall()
      return note if note else None
    except Exception as e:
      print(f"Error retrieving note: {e}")
      return None

def retrieve_antepartuminformation_note(connection, encounter_id):
    try:
        with connection.cursor() as cursor:
            # SQL query to select note according to mother id and encounter id
            query = f"SELECT note, note_title FROM child_structured_data_2022.mother_notes WHERE mother_encounter_id = {encounter_id} AND note_title = 'antepartuminformation'"
            cursor.execute(query)
            notes = cursor.fetchall()
        return notes if notes else None
    except Exception as e:
        print(f"Error retrieving note: {e}")
        return None

#Function to retrieve delivery note from the FHR database
def retrieve_delivery_note(connection, encounter_id):
    try:
      with connection.cursor() as cursor:
        # SQL query to select note according to mother id and encounter id
        query = f"SELECT note, note_title FROM child_structured_data_2022.mother_notes WHERE mother_encounter_id = {encounter_id} AND (note_title LIKE '%delivery%' OR note_title LIKE '%discharge%' OR note_title LIKE '%opnote%')"
        cursor.execute(query)
        note = cursor.fetchall()
      return note if note else None
    except Exception as e:
      print(f"Error retrieving note: {e}")
      return None

#Function to retrieve all note titles from FHR database where note_title matches specific string
def retrieve_note_titles(connection):
    try:
      with connection.cursor() as cursor:
        # SQL query to select note according to mother id and encounter id
        query = f"SELECT mother_encounter_id, note_title, note FROM child_structured_data_2022.mother_notes WHERE note_title LIKE '%admission%' OR note_title LIKE '%h&p%' LIMIT 20"
        cursor.execute(query)
        notetitles = cursor.fetchall()
      return notetitles if notetitles else None
    except Exception as e:
      print(f"Error retrieving note: {e}")
      return None

