# This file is __init__.py in the app/pages directory
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'jai123'
    from .pages.routes import pages
    app.register_blueprint(pages)

    return app
