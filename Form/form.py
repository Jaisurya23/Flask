from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
app = Flask(__name__)
secret_key = os.environ.get('SECRET_KEY','jai123')
app.secret_key = secret_key
@app.route('/')
def login_page():
    return render_template('login.html', title='Login Page', heading='User Login Form')

@app.route('/submit', methods=['POST'])
def submit_login():
    name = request.form.get('name')
    father_name = request.form.get('father_name')
    mother_name = request.form.get('mother_name')
    age = request.form.get('age')
    email = request.form.get('email')
    education = request.form.get('education')
    mark = request.form.get('marks')
    address = request.form.get('address')
    if not name or not father_name or not mother_name or not age or not email or not education or not mark or not address:
        flash('All fields are required!', 'error')
        return redirect(url_for('login_page'))
    flash('Form submitted successfully!', 'success')
    session['name'] = name
    session['father_name'] = father_name
    session['mother_name'] = mother_name
    session['age'] = age
    session['email'] = email
    session['education'] = education
    session['mark'] = mark
    session['address'] = address
    return redirect(url_for('output'))
@app.route('/result')
def output():
    name = session.get('name', 'Guest')
    father_name = session.get('father_name', 'Not provided')
    mother_name = session.get('mother_name', 'Not provided')    
    age = session.get('age', 'Not provided')
    email = session.get('email', 'Not provided')
    education = session.get('education', 'Not provided')
    mark = session.get('mark', 'Not provided')
    address = session.get('address', 'Not provided')
    return render_template('result.html', title='Result', heading='Form Submission Result',
                           name=name, father_name=father_name, mother_name=mother_name,
                           age=age, email=email, education=education, mark=mark, address=address)
if __name__ == '__main__':
    app.run(debug=True)