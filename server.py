from flask import Flask, render_template, request, url_for, redirect, flash
from wtforms import *
from models import *
from flask import session
import hashlib
import re
import sys

import model.query_functs

app = Flask(__name__)
app.secret_key = 'key'
app.config.update(dict(
    USERNAME='admin',
    PASSWORD='21232f297a57a5a743894a0e4a801fc3'
))


def validate(name):
    pattern = r"^([a-z]|[A-Z]|[áéíóőÁÉÍÓŐ]+[,.]?[ ]?|[a-z][áéíóőÁÉÍÓŐ]+['-]?)+$"
    if re.match(pattern, name):
        return True
    else:
        return False


def emailvalidate(mail):
    pattern = r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"
    if re.match(pattern, mail):
        return True
    else:
        return False


def digest(message):
    dig = hashlib.md5(str(message).encode('UTF-8'))
    return dig.hexdigest()


@app.route('/admin/login', methods=['GET', 'POST'])
def login():
    error = None
    form = MyForm(request.form, csrf_enabled=False)
    if request.method == 'POST':
        if form.username.data != app.config['USERNAME'] or digest(form.password.data) != app.config['PASSWORD']:
            error = 'Invalid username or password!'
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
    applicant_first_name = StringField('Applicant First Name')
    applicant_last_name = StringField('Applicant Last Name')
    applicant_app_code = StringField('Applicant AppCode')
    applicant_email = StringField('Applicant Email')
    applicant_city = StringField('Applicant City')
    applicant_school = StringField('Applicant School')
    applicant_interview = StringField('Applicant Interview')


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
            data_list.append(entry.recipient_name)
            data_list.append(entry.recipient_email)
            data_list.append(entry.subject)
            data_list.append(entry.content)
            data_list.append(entry.mode)
            data_list.append(entry.timestamp.strftime('%y-%m-%d  %H:%M'))
            if entry.status:
                data_list.append('Sent')
            else:
                data_list.append('Not Sent')
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
    if not validate(form.first_name.data):
        flash('Invalid First name format')
    if not validate(form.last_name.data):
        flash('Invalid Last name format')
    if not validate(form.city.data):
        flash('Invalid City name format')
    if emailvalidate(form.email.data) is False or Applicant.select().where(Applicant.email == form.email.data).exists():
        flash('Invalid or registered email address!')
    print(form.validate())
    if '_flashes' not in session:
        Applicant.create(first_name=form.first_name.data, last_name=form.last_name.data,
                         city=form.city.data, email=form.email.data, status='new')
        flash("Registration successful!")
        return redirect(url_for('home'))

    return render_template('applicant_form.html', form=form)


@app.route('/admin/applicants', methods=['GET', 'POST'])
def list_applicants():
    if session['logged_in']:
        if request.method == 'POST':
            form = MyForm(request.form, csrf_enabled=False)

            interview_ids = [0]
            for interview in Interview.select():
                if str(form.applicant_interview.data) in str(interview.start):
                    interview_ids.append(interview.id)
            query = model.query_functs.filter_applicants(form, interview_ids)
        else:
            form = MyForm()
            query = Applicant.select().join(School, JOIN.LEFT_OUTER).switch(Applicant).join(Interview, JOIN.LEFT_OUTER)

        entries = []
        for applicant in query:
            data_list = []
            data_list.append(applicant.id)
            data_list.append(applicant.application_code)
            data_list.append(applicant.first_name + " " + applicant.last_name)
            data_list.append(applicant.email)
            data_list.append(applicant.city)
            try:
                data_list.append(applicant.school.location)
            except AttributeError:
                data_list.append("Not yet set")
            try:
                data_list.append(applicant.interview_slot.start)
            except AttributeError:
                data_list.append("Not yet set")

            entries.append(data_list)

        return render_template('applicant_filter.html', title="Applicants", entries=entries,
                               titles=["Application Code", "Name", "Email", "City", "School", "Interview time"],
                               form=form)
    return redirect(url_for('home'))


@app.route('/admin/applicants/add_school/<id>', methods=['POST'])
def add_school(id):
    from code_gener import solution, passwordgen
    if session['logged_in']:
        applicant = Applicant.select().where(id == Applicant.id)[0]
        applicant.application_code = solution()
        applicant.save()
        applicant.set_city()
    return redirect(url_for('list_applicants'))


@app.route('/admin/applicants/add_interview/<id>', methods=['POST'])
def add_interview(id):
    from models import Applicant
    if session['logged_in']:
        applicant = Applicant.select().where(id == Applicant.id)[0]
        if not applicant.assign_slot_with_mentors():
            flash('Not enough interview slot at the assigned school!')
    return redirect(url_for('list_applicants'))


@app.route('/admin/applicants/delete_applicant/<id>', methods=['POST'])
def delete_applicant(id):
    print(id)
    if session['logged_in']:
        applicant = Applicant.select().where(Applicant.id == id)[0]
        try:
            interview = Interview.select().where(Interview.id == applicant.interview_slot)[0]
            interview.free = True
            interview.save()
            AssignMentor.delete().where(AssignMentor.interview == interview).execute()
        except IndexError:
            pass

        Question.delete().where(Question.applicant == applicant).execute()

        Applicant.delete().where(Applicant.id == id).execute()
        return redirect(url_for('list_applicants'))


@app.route('/admin/applicants/assign_schools_all', methods=['post'])
def assign_school_all():
    if session['logged_in']:
        Applicant.finding_city()
        Applicant.set_app_code()
    return redirect(url_for('list_applicants'))


@app.route('/admin/applicants/assign_interview_all', methods=['post'])
def assign_interview_all():
    if session['logged_in']:
        Applicant.assign_interview_slot()
    return redirect(url_for('list_applicants'))


if __name__ == '__main__':
    app.run(host='192.168.0.234', port='5000')
