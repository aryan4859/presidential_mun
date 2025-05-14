# routes/view.py
from flask import Blueprint, render_template
from models.database import get_db

view_bp = Blueprint('view', __name__)

@view_bp.route('/view')
def view_registrations():
    db, cursor = get_db()
    cursor.execute("SELECT * FROM registrations ORDER BY id DESC")
    data = cursor.fetchall()
    return render_template('view_registration.html', registrations=data)