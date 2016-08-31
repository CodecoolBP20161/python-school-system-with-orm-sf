from flask import Flask, render_template, request, url_for, redirect, g
from wtforms import *
from models import *
from datetime import datetime

app = Flask(__name__)


class MyForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    city = StringField('City')
    email = StringField('Email', validators=[validators.Email(message='Invalid email address!')])
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
    query = {}
    for entry in EmailLog.select():
        query['subject'] = entry.subject
        query['content'] = entry.content
        query['mode'] = entry.mode
        query['time'] = entry.datetime.timestamp
        query['receipant_name'] = entry.receipant_name
        query['receipant_email'] = entry.receipant_email
        query['status'] = entry.status

    return render_template('email_log.html', entry=entry)


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
    return redirect(url_for('applicant_form'))


if __name__ == '__main__':
    app.run()
