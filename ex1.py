from flask import Flask, render_template, request, redirect, url_for, flash
import os
app = Flask(__name__)
secret_key = os.environ.get('SECRET_KEY', 'jai123')
app.secret_key = secret_key

@app.route('/')
def home():
    return render_template('ex1.html', title ="Login page", heading = "Login page")

@app.route('/login', methods = ['POST'])
def submit_form():
    user_name = "user"
    password = "admin123"
    if request.method == 'POST':
        name = request.form.get('name')
        passw = request.form.get('password')
        if name == user_name and passw == password:
            flash(f'Login successful! Welcome {name}', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed! Please check your credentials.', 'danger')
            return redirect(url_for('home'))
        
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', title='Result', heading='Login Result')

if __name__ == '__main__':
    app.run(debug=True)