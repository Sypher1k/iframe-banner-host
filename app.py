from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    files = os.listdir(UPLOAD_FOLDER)
    print(files)
    return render_template('home.html',file=files)