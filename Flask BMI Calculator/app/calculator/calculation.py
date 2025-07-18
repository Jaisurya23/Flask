# This file is calculation.py in a Flask application for handling BMI calculations.
from flask import Blueprint, request, session, flash, redirect, url_for, render_template

app = Blueprint('calculator', __name__)

# Route to handle form POST
@app.route('/calculate', methods=['POST'])
def input():
    session['name'] = request.form.get('name')
    session['age'] = request.form.get('age')
    session['weight'] = request.form.get('weight')
    session['height'] = request.form.get('height')

    if not session['name'] or not session['age'] or not session['weight'] or not session['height']:
        flash('All fields are required!', 'error')
        return redirect(url_for('form.home'))

    return redirect(url_for('calculator.calculate_bmi'))


# Route to do the BMI calculation
@app.route('/bmi')
def calculate_bmi():
    try:
        weight = float(session.get('weight', 0))
        height = float(session.get('height', 0)) / 100  # cm to meters

        bmi = round(weight / (height ** 2), 2)
        session['bmi'] = bmi  # Store result in session
    except:
        flash('Invalid input! Please enter numbers.', 'error')
        return redirect(url_for('form.home'))

    return redirect(url_for('calculator.output'))


# Route to show the result
@app.route('/result')
def output():
    name = session.get('name', 'Guest')
    age = session.get('age', 'Unknown')
    weight = session.get('weight', 'Unknown')
    height = session.get('height', 'Unknown')
    bmi = session.get('bmi', None)

    category = ''
    if bmi:
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi < 24.9:
            category = 'Normal weight'
        elif 25 <= bmi < 29.9:
            category = 'Overweight'
        else:
            category = 'Obesity'

    return render_template('result.html', title = "BMI Result", heading = "Your result " ,name=name, age=age, weight=weight, height=height, bmi=bmi, category=category)
