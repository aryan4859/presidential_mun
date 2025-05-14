import getpass
from werkzeug.security import generate_password_hash
import mysql.connector

# Database credentials
DB_HOST = "localhost"
DB_USER = "mun_user"
DB_PASSWORD = "securepassword"  # Replace with actual password
DB_NAME = "presidential_mun"

# Get user input
username = input("Enter admin username: ")
password = getpass.getpass("Enter admin password (hidden): ")

# Generate hashed password
hashed_password = generate_password_hash(password)
print(f"[+] Password hash generated.")

try:
    # Connect to database
    db = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = db.cursor()

    # Delete existing user if present
    cursor.execute("DELETE FROM users WHERE username = %s", (username,))
    print(f"[-] Deleted old user (if existed): {username}")

    # Reset auto increment (optional)
    cursor.execute("ALTER TABLE users AUTO_INCREMENT = 1")

    # Insert new user
    cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
    db.commit()

    print(f"[+] New admin user created: {username}")
except mysql.connector.Error as err:
    print(f"[!] MySQL Error: {err}")
finally:
    if cursor:
        cursor.close()
    if db:
        db.close()
