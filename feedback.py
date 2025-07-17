from flask import Flask, render_template, request, redirect, url_for, flash, session
import os

app = Flask(__name__)
# Use a more secure way to set the secret key
app.secret_key = os.environ.get('SECRET_KEY', 'jai123')

@app.route('/')
def home():
    return render_template('feedback_form.html', title='User Form', heading='User Information Form')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form.get('name')
    email = request.form.get('email')
    feedback = request.form.get('feedback')
    session['name'] = name
    session['email'] = email    
    session['feedback'] = feedback
    flash(f'Thanks for your feedback, {name}!', 'success')
    return redirect(url_for('thank_you'))
@app.route('/thankyou')
def thank_you():
    name = session.get('name', 'Guest')
    email = session.get('email', 'No email provided')
    feedback = session.get('feedback', 'No feedback provided')
    return render_template('thankyou.html', title='Thank You', heading='Thank You for Your Feedback!', name=name, email=email, feedback=feedback)

if __name__ == '__main__':
    app.run(debug=True)