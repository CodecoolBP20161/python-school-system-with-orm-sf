from flask import Flask, render_template, request, url_for, redirect, g
from wtforms import *
from models import *

app = Flask(__name__)


class MyForm(Form):
    first_name = StringField('Firs Name')
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


def get_db(database=db):
    return database


@app.route('/registration', methods=['GET'])
def applicant_form():
    return render_template('applicant_form.html', form=form)


@app.route('/registration/submit', methods=['POST'])
def submit_applicant():
    form = MyForm(request.form, csrf_enabled=False)
    if form.validate():
        Applicant.create(first_name=form.first_name, last_name=form.last_name,
                         city=form.city, email=form.email, status='new')
        return redirect(url_for('home'))
    return redirect(url_for('applicant_form'))


if __name__ == '__main__':
    app.run()
