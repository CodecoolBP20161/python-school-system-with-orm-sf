from flask import Flask, render_template, request, url_for, redirect, flash
from wtforms import *
from models import *
from datetime import datetime
from flask import session
import hashlib


app = Flask(__name__)
app.secret_key = 'key'
app.config.update(dict(
    USERNAME='admin',
    PASSWORD='21232f297a57a5a743894a0e4a801fc3'
))


def digest(message):
    dig = hashlib.md5(str(message).encode('UTF-8'))
    return dig.hexdigest()



@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    error = None
    form = MyForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        if form.username.data != app.config['USERNAME']:
            error = 'Invalid username'
        elif digest(form.password.data) != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('admin'))
    return render_template('admin_login.html', error=error, form=form)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('home'))


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')


class MyForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    city = StringField('City')
    email = StringField('Email', validators=[validators.Email()])
    submit = SubmitField()


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin/email-log', methods=['GET'])
def email_log():
    if session['logged_in']:
        mylist = []
        for entry in EmailLog.select():
            data_list = []
            data_list.append(entry.subject)
            data_list.append(entry.content)
            data_list.append(entry.mode)
            data_list.append(entry.timestamp)
            data_list.append(entry.recipient_name)
            data_list.append(entry.recipient_email)
            data_list.append(entry.status)
            mylist.append(data_list)
        return render_template('listing.html', title="Email log", entries=mylist,
                               titles=["Recipient's name", "Recipient's email", "Email Subject",
                                       "Email Content", "Email Type", "Time", "Status"])
    return redirect(url_for('admin'))


def get_db(database=db):
    return database


@app.route('/registration', methods=['GET'])
def applicant_form():
    form = MyForm()
    return render_template('applicant_form.html', form=form)


@app.route('/registration/submit', methods=['POST'])
def submit_applicant():
    form = MyForm(request.form, csrf_enabled=False)
    if form.validate():
        Applicant.create(first_name=form.first_name.data, last_name=form.last_name.data,
                         city=form.city.data, email=form.email.data, status='new')
        return redirect(url_for('home'))
    flash('Invalid email address!')
    return render_template('applicant_form.html', form=form)


if __name__ == '__main__':
    app.run()
