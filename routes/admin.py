#routes/admin.py
from flask import Blueprint, request, render_template, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
from models.database import get_db
from utils.helpers import encode_auth_token
from utils.decorators import token_required  

admin_bp = Blueprint('admin', __name__)

# Login route
@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': 
        data = request.form

        if not data or not data.get('username') or not data.get('password'):
            flash('Missing username or password', 'danger')
            return redirect(url_for('admin.login'))

        username = data.get('username')
        password = data.get('password')
        
        db, cursor = get_db()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user['password'], password): 
            token = encode_auth_token(user['id'])
            flash('Login successful', 'success') 
            return redirect(url_for('admin.view_registrations', token=token))  
        else:
            flash('Invalid credentials', 'danger')
            return redirect(url_for('admin.login'))

    return render_template('login.html') 

# /registration
@admin_bp.route('/registration', methods=['GET', 'POST'])
def register_admin():
    if request.method == 'POST':
        data = request.form
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            flash('Missing username or password', 'danger')
            return redirect(url_for('admin.register_admin'))

       
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        db, cursor = get_db()
        cursor.execute('INSERT INTO users (username, password) VALUES (%s, %s)', (username, hashed_password))
        db.commit()

        flash('Admin registered successfully!', 'success')
        return redirect(url_for('admin.login')) 

    return render_template('adminreg.html')  

# View registrations route
@admin_bp.route('/registrations')
@token_required
def view_registrations(user_id):
    db, cursor = get_db()
    cursor.execute("SELECT * FROM registrations")
    registrations = cursor.fetchall()
    print("Registrations:", registrations)

    return render_template('view_registrations.html', registrations=registrations)
