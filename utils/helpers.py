import os
from dotenv import load_dotenv
import jwt
import datetime

# Load environment variables from .env file
load_dotenv()

# Retrieve the SECRET_KEY from environment variables
SECRET_KEY = os.getenv('SECRET_KEY')

if not SECRET_KEY:
    raise ValueError("No SECRET_KEY set in environment variables")

def allowed_file(filename):
    """
    Check if the file is allowed based on its extension.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'pdf', 'png', 'jpg', 'jpeg'}

def encode_auth_token(user_id):
    """
    Generates the Auth Token for a user
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Token expires in 1 day
            'iat': datetime.datetime.utcnow(),
            'sub': user_id  # Subject is the user_id
        }
        # Ensure the token is returned as a string
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        return token.decode('utf-8') if isinstance(token, bytes) else token
    except Exception as e:
        return str(e)

def decode_auth_token(auth_token):
    """
    Decodes the Auth Token to get the user_id
    """
    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']  # Return the user_id from the payload
    except jwt.ExpiredSignatureError:
        return 'Token has expired'
    except jwt.InvalidTokenError:
        return 'Invalid token'
    except Exception as e:
        return str(e) 
