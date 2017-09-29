from flask import Flask, request, redirect, render_template
import html

app = Flask(__name__)
app.config['DEBUG'] = True

username = ''


def valid_entry(text):
    if text:
        if ' ' not in text:
            if 2 < len(text) < 21:
                if ' ' not in text:
                    return True
    else:
        return False


def valid_email(address):
    if address.count('@') == 1:
        if address.count('.') == 1:
            if ' ' not in address:
                if 2 < len(address) < 21:
                    return True
    return False


@app.route("/", methods=['GET'])
def index():
    return render_template('signup-form.html')


@app.route("/confirmation", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    password_confirm = request.form['password-confirm']
    email = request.form['email']

    username_error = ''
    password_error = ''
    confirm_error = ''
    email_error = ''
    error = False

    if not valid_entry(username):
        username_error = 'Invalid username!'
        error = True

    if not valid_entry(password):
        password_error = "Invalid password!"
        error = True

    if password != password_confirm:
        confirm_error = "Passwords do not match!"
        error = True

    if email:
        if not valid_email(email):
            email_error = "Invalid email!"
            email = ''
            error = True

    if error:
        return render_template('signup-form.html', username=username and html.escape(username, quote=True),
                               username_error=username_error and html.escape(username_error, quote=True),
                               password_error=password_error and html.escape(password_error, quote=True),
                               confirm_error=confirm_error and html.escape(confirm_error, quote=True),
                               email_error=email_error and html.escape(email_error, quote=True),
                               email=email and html.escape(email, quote=True))

    return render_template('confirmation.html', username=username)


app.run()
