# models/database.py
import os
from dotenv import load_dotenv
import mysql.connector
load_dotenv()
def get_db():
    db = mysql.connector.connect(
        host=os.getenv('host'),
        user=os.getenv('user'),
        password=os.getenv('password'),   
        database=os.getenv('database')
    )
    cursor = db.cursor(dictionary=True) 
    return db, cursor
