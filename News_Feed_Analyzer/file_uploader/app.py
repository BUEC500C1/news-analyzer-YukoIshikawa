from flask import Flask
import os

UPLOAD_FOLDER = 'C:/Users/<User Name>/Desktop/News_Feed_Analyzer/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
basedir = os.path.abspath(os.path.dirname(__file__))