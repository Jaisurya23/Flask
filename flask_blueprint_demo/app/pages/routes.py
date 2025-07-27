# This file is routes.py in the app/pages directory
from flask import Flask, render_template, flash, Blueprint
pages = Blueprint('pages', __name__)
@pages.route('/')
def home():
    flash("Welcome to the Jaisurya's Flask App!", 'info')
    return render_template('about.html', title='Home Page', heading='Welcome to the Home Page')
