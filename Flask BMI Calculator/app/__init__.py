# This file is __init__.py in a Flask application for setting up the app and registering blueprints.
from flask import Flask
app = Flask(__name__)
app.secret_key='secret_key'
def create_app():
    from app.calculator.calculation import app as calculator_blueprint
    from app.form.form import app as form_blueprint

    app.register_blueprint(calculator_blueprint)
    app.register_blueprint(form_blueprint)

    return app