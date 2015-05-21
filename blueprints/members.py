from flask import Blueprint, render_template, redirect, session


blueprint = Blueprint('members', __name__, url_prefix='/members')

@blueprint.before_request
def check_auth():
    if not 'user' in session:
        return redirect('/login')

@blueprint.route('/')
def view_membersarea():
    return render_template('members/members.html', title='Members Area')