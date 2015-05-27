from flask import Blueprint, redirect, session, render_template, flash

from util.auth import Auth
from forms.login import LoginForm

# Used simply for creating a test user, remove it when project is complete
from loader import db
from models import Member
from datetime import datetime

blueprint = Blueprint('bp_auth', __name__)

@blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if Auth.check(form.username.data, form.password.data):
            Auth.login(form.username.data, form.password.data)
        else:
            flash('Invalid credentials.')

        if 'user' in session and session['user'].priv_level >= Auth.member:
            return redirect('/members')

        if 'user' in session and session['user'].priv_level <= Auth.admin:
            return redirect('/admin')

    return render_template('login.html', form=form, hideback=True)


@blueprint.route('/logout')
def logout():
    Auth.logout()

    flash('You have been logged out.')

    return redirect('/login')

'''# This can be treated as an example of how to create a user/how to add something to the database. However, we aren't
# going to be using this particular function other than for testing purposes
@blueprint.route('/mktestuser')
def mktestuser():

    user = Member()
    user.password = Auth.hash_password("mike")
    user.cid = '003784312'
    user.fname = 'Mike'
    user.lname = 'Korcha'
    user.email_csusb = 'korcham@coyote.csusb.edu'
    user.email_primary = 'mikekorcha@gmail.com'
    user.standing = 'Graduate'
    user.gender = 'Male'
    user.shirt_size = 'M'
    user.shirt_received = datetime.utcfromtimestamp(0)
    user.majors = 'Computer Science'
    user.paid_until = datetime.utcfromtimestamp(0)
    user.created = datetime.utcnow()
    user.role = Auth.admin

    db.session.add(user)
    db.session.commit()

    return "Done. username=\"cowbell\", password=\"cowbell\""'''

