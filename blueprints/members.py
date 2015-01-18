from flask import Blueprint, render_template, redirect, url_for, session

from util.auth import Auth
from forms.login import LoginForm

# Used simply for creating a test user, remove it when project is complete
from loader import db
from models.user import User
from datetime import datetime

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
@blueprint.route('/index')
def index():
    form = LoginForm()

    return render_template('login.html', form=form)


@blueprint.route('/login', methods=["POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if Auth.check(form.username.data, form.password.data):
            Auth.login(form.username.data, form.password.data)

        if session['user'].role >= Auth.member:
            return redirect('/')

        if session['user'].role <= Auth.admin:
            return redirect('/admin/')

    return redirect('/')


@blueprint.route('/logout')
def logout():
    Auth.logout()
    return redirect('/')

# This can be treated as an example of how to create a user/how to add something to the database. However, we aren't
# going to be using this particular function other than for testing purposes
@blueprint.route('/mktestuser')
def mktestuser():

    user = User()
    user.username = "mike"
    user.password = Auth.hash_password("mike")
    user.email = 'mike@example.com'
    user.created = datetime.now()
    user.role = 0

    db.session.add(user)
    db.session.commit()

    return "Done. username=\"cowbell\", password=\"cowbell\""