# This file is form.py in a Flask application for handling form input.
from flask import Blueprint, request, render_template
app = Blueprint('form', __name__)
@app.route('/')
def home():
    return render_template('form.html', title='BMI Calculator', heading='BMI Calculator')
