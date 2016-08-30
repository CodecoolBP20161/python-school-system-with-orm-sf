from flask import Flask, render_template, request, url_for, redirect, g
from wtforms import *
from connect import db
from models import *

app = Flask(__name__)


class MyForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    city = StringField('City')
    email = StringField('Email')
    submit = SubmitField()


@app.before_request
def before_request():
    db.connect()


@app.after_request
def after_request(response):
    db.close()
    return response


@app.route('/')
def main():
    return "HOME"


if __name__ == '__main__':
    app.run()
