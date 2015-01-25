from flask import session

from datetime import datetime

from loader import app
from models.content import Content
from sqlalchemy import and_

from util.auth import Auth

@app.template_global()
def get_year():
    return datetime.now().year

@app.template_global()
def get_loggedin():
    return True if 'user' in session else False

@app.template_global()
def get_admin():
    return True if 'user' in session and session['user'].role <= Auth.admin else False

@app.template_global()
def get_name():
    return session['user'].fname + ' ' + session['user'].lname

@app.template_global()
def get_nav(level):
    return Content.query.filter(and_(Content.in_navigation == True, Content.require_level == level))