from flask import Flask, render_template, request, redirect, url_for, flash
import re

app = Flask(__name__)
app.secret_key = "secretkey123"

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    errors = {}

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        event = request.form.get('event')
        comments = request.form.get('comments')

        # Validation
        if not name or len(name) < 3:
            errors['name'] = "Name must be at least 3 characters long."

        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not email or not re.match(email_pattern, email):
            errors['email'] = "Enter a valid email address."

        if not phone or not phone.isdigit() or len(phone) != 10:
            errors['phone'] = "Phone number must be exactly 10 digits."

        if not event:
            errors['event'] = "Please select an event."

        if not errors:
            flash("Registration Successful!", "success")
            return redirect(url_for('confirmation', name=name, event=event))

    return render_template('register.html', errors=errors)

@app.route('/confirmation')
def confirmation():
    name = request.args.get('name')
    event = request.args.get('event')
    return render_template('confirmation.html', name=name, event=event)

if __name__ == '__main__':
    app.run()
