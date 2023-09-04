import os
from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message

from contact_form import ContactForm, csrf

mail = Mail()

app = Flask(__name__)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
csrf.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourID@xmail.com'
app.config['MAIL_PASSWORD'] = "*****'_"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        subject = form.subject.data
        message = form.message.data

        send_message(name, email, subject, message)
        return redirect('/success')

    return render_template('contact.html', form=form)


@app.route('/success')
def success():
    return render_template('base.html')


def send_message(name, email, subject, message):
    msg = Message(subject, sender=email, recipients=[
                  'recipientID@xmail.com'], body=message)
    mail.send(msg)


if __name__ == "__main__":
    app.run(debug=True)
