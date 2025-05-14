# models/database.py
import mysql.connector

def get_db():
    db = mysql.connector.connect(
        host="localhost",
        user="mun_user",
        password="securepassword",  # Replace with your MySQL password
        database="presidential_mun"
    )
    cursor = db.cursor(dictionary=True)  # Use dictionary cursor to return results as dictionaries
    return db, cursor
