from flask import Flask, render_template, request, redirect, url_for,flash
secret_key = 'jai123'
app = Flask(__name__)
app.secret_key = secret_key
@app.route('/')
def home():
    return render_template('form.html', title='User Form', heading='User Information Form')

@app.route('/submit', methods=['POST'])
def submit_form():
    name = request.form['name']
    email = request.form['email']
    flash(f'Form submitted successfully! Name: {name}, Email: {email}', 'success')
    return redirect(url_for('process_form'))

@app.route('/thankyou')
def process_form():
    return render_template('thankyou.html')
if __name__ == '__main__':
    app.run(debug=True)