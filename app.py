import os

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return (
        'Angelo Daniel' "</br>"
        'BSIT - 3 2nd 25' "</br>"
        'System Integrations' "</br>"
        'Semi Final Exams' "</br>"
    )