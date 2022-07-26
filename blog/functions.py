from django.utils.crypto import get_random_string
import sqlite3
from sqlite3 import Error

# Create connection to database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

# Insert new file into database
def insert_into_db(conn, filename, formData):
    sql = 'INSERT INTO uploads( title, content,filename) VALUES( "' + formData['title'] + '",   "' + formData['content'] + '","' + filename + '");'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    return cur.lastrowid

# Save uploaded file
def handle_uploaded_file(f, formData):  
    ext = f.name.split(".")[-1]
    filename = get_random_string(length=13) + "." + ext
    with open('media/'+ filename, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    submit(filename, formData)

# Submit uploaded file
def submit(file, formData):
    db_location = r"./media_upload.db"
    conn = create_connection(db_location)
    with conn:
        result = insert_into_db(conn, file, formData)
    return result

# Load all files
def load_files(conn):
    sql = 'SELECT * FROM uploads;'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    return rows






