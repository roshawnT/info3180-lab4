import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()
# Config Values
USERNAME = 'admin'
PASSWORD = 'password123'

# SECRET_KEY is needed for session security, the flash() method in this case stores the message in a session
SECRET_KEY = 'Sup3r$3cretkey'
ALLOWED_EXTENSIONS = {'png', 'jpg','jpeg'}
UPLOAD_FOLDER = './app/static/uploads'


app = Flask(__name__)
app.config.from_object(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from app import views


