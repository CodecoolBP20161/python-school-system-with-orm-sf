from flask import Flask, render_template, request, url_for, redirect, g
from wtforms import *

app = Flask(__name__)



class MyForm(Form):
    first_name = TextField('Firs Name')
    last_name = TextField('Last Name')
    city = TextField('City')
    email = EmailField('Email')
    submit = SubmitField()


@app.route('/')
def main():
    return 'YEAHH!!!!'


if __name__ == '__main__':
    app.run()
