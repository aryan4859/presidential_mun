# app.py
from flask import Flask
from routes.registration import registration_bp 
from routes.view import view_bp 
from routes.index import index_bp  
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.secret_key = os.getenv("SECRET_KEY")

if not app.secret_key:
    raise ValueError("SECRET_KEY is not set. Please define it in the .env file.")

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static/uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(index_bp)  
app.register_blueprint(registration_bp)
app.register_blueprint(view_bp) 

@app.route('/')
def home():
    return "Welcome to Presidential MUN API"

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        try:
            os.makedirs(UPLOAD_FOLDER)
        except OSError as e:
            print(f"Error creating upload folder: {e}")
            raise

    debug_mode = os.getenv("DEBUG", "False").lower() == "true"
    app.run(debug=debug_mode)

