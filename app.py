# app.py
from flask import Flask
from routes.registration import registration_bp
from routes.view import view_bp
from routes.admin import admin_bp
import os 

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY") 

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(registration_bp)
app.register_blueprint(view_bp)

 
app.register_blueprint(admin_bp, url_prefix='/admin')

@app.route('/')
def home():
    return "Welcome to Presidential MUN API" 

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)  

