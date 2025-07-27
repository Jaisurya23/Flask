# This file is run.py in the root directory of the Flask application
from app import create_app
app = create_app()
if __name__ == '__main__':
    app.run(debug=True)