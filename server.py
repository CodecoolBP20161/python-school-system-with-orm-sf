from flask import Flask, render_template, request, url_for, redirect, flash
from wtforms import *
from models import *
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'key'


class MyForm(Form):
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
    dict_query = {}
    for entry in EmailLog.select():
        dict_query['subject'] = entry.subject
        dict_query['content'] = entry.content
        dict_query['mode'] = entry.mode
        dict_query['time'] = entry.timestamp
        dict_query['receipant_name'] = entry.receipant_name
        dict_query['receipant_email'] = entry.receipant_email
        dict_query['status'] = entry.status

    return render_template('email_log.html', entries=dict_query)


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
