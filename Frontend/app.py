from functools import wraps
from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mail import Mail, Message
from random import randrange
import pickle

from database import insert_user, find_user, find_user_by_email, update_password_by_email

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