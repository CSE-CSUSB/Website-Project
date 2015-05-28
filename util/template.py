from flask import session

from datetime import datetime

from loader import app
from models import Content
from sqlalchemy import and_

from util.auth import Auth

@app.template_global()
def get_year():
    return datetime.now().year

@app.template_global()
def is_loggedin():
    return True if 'user' in session else False

@app.template_global()
def is_admin():
    return True if 'user' in session and session['user'].priv_level <= Auth.admin else False

@app.template_global()
def get_name():
    return session['user'].fname + ' ' + session['user'].lname

@app.template_global()
def get_nav(level):
    return Content.query.filter(and_(Content.show_in_nav == 1, Content.required_priv_level == level))