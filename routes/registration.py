from flask import Blueprint, request, render_template, redirect, url_for, flash, current_app
from werkzeug.utils import secure_filename
from models.database import get_db
from utils.helpers import allowed_file
import os

registration_bp = Blueprint('registration', __name__)

@registration_bp.route('/register', methods=['GET'])
def register():
    committees = [
        "UNGA", "UNSC", "UNHRC", "DISEC", "Lok Sabha",
        "International Press", "AIPPM", "WHO"
    ]
    return render_template('register.html', committees=committees)


@registration_bp.route('/register', methods=['POST'])
def register_post():
    form = request.form
    file = request.files.get('payment_receipt')

    if not file or not allowed_file(file.filename):
        flash('Invalid or missing payment receipt file.')
        return redirect(url_for('registration.register'))  # Fixed redirect to the correct route

    filename = secure_filename(file.filename)
    filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    db, cursor = get_db()

    sql = """
        INSERT INTO registrations (
            first_name, last_name, email, current_address, dob,
            phone1, phone2, whatsapp, food_pref, prev_college,
            stream, prev_mun, primary_committee, secondary_committee,
            contrib_view, future_goals, medical, payment_receipt_path
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                  %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        form.get('first_name'),
        form.get('last_name'),
        form.get('email'),
        form.get('current_address'),
        form.get('dob'),
        form.get('phone1'),
        form.get('phone2'),
        form.get('whatsapp'),
        form.get('food_pref'),
        form.get('prev_college'),
        form.get('stream'),
        form.get('prev_mun'),
        form.get('primary_committee'),
        form.get('secondary_committee'),
        form.get('contrib_view'),
        form.get('future_goals'),
        form.get('medical'),
        filepath
    )

    try:
        cursor.execute(sql, values)
        db.commit()
        flash('Registration successful!')
    except Exception as e:
        print(f"[ERROR] Database insertion failed: {e}")
        flash('Something went wrong. Try again.')
    finally:
        cursor.close()

    return redirect(url_for('registration.register'))  # Fixed redirect to the correct route
