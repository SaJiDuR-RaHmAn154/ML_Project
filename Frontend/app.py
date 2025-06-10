from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mail import Mail, Message
from random import randrange
import pickle
from datetime import datetime
import pytz
import os
import random

from database import insert_user, find_user_by_email, update_password_by_email, get_user_profile, get_checkup_history, add_checkup_history,delete_checkup_history

app = Flask(__name__)
app.secret_key = "CardioInsight"

# --- Flask-Mail configuration for sending emails ---
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "shareserial120@gmail.com"
app.config["MAIL_PASSWORD"] = "wvxh fsvs yfwx zhwk"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True
app.config['SESSION_PERMANENT'] = False

mail = Mail(app)

# --- File upload configuration ---
UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Decorator to require login for certain routes ---
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login', msg="Please login to access this page."))
        return f(*args, **kwargs)
    return decorated_function

# --- Home page route ---
@app.route("/")
def home():
    msg = request.args.get("msg")  
    if request.args.get("guest") == "1":
        session.pop('username', None)
        name = "Guest"
    elif 'username' in session:
        name = session['username']
    else:
        name = "Guest"
    return render_template("home.html", name=name, msg=msg)

# --- Prediction form page (requires login) ---
@app.route("/find")
@login_required
def find():
    return render_template("find.html", name=session.get("username", "Guest"))