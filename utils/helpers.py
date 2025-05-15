import os
from dotenv import load_dotenv
import jwt
import datetime

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set in environment variables")

def allowed_file(filename):
    """
    Check if the file is allowed based on its extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'png', 'jpg', 'jpeg'}

