from flask import Blueprint, redirect, session, render_template

from util.auth import Auth
from forms.login import LoginForm

# Used simply for creating a test user, remove it when project is complete
from loader import db
from models.user import User
from datetime import datetime

blueprint = Blueprint('members', __name__)

@blueprint.route('/login', methods=["POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if Auth.check(form.username.data, form.password.data):
            Auth.login(form.username.data, form.password.data)

        if 'user' in session and session['user'].role >= Auth.member:
            return redirect('/')

        if 'user' in session and session['user'].role <= Auth.admin:
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

@blueprint.route('/test')
def testlayout():
    return render_template('member/layout.html')
