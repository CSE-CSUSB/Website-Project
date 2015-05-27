from loader import app, db
from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

from util.auth import Auth

from models import *

from flask import Blueprint, render_template, redirect, session, flash

blueprint = Blueprint('bp_admin2', __name__, url_prefix='/admin2')

class MyView(BaseView):
    def is_accessible(self):
        if 'user' in session:
            if session['user'].priv_level < Auth.member:
                return True

    @expose('/')
    def index(self):
        return self.render('admin/index.html')

admin = Admin(app, name='Officers Page', url='/admin2')
admin.add_view(ModelView(Club, db.session, category='Direct DB Table Access'))
admin.add_view(ModelView(Member, db.session, category='Direct DB Table Access'))
admin.add_view(ModelView(Content, db.session, category='Direct DB Table Access'))
admin.add_view(ModelView(Event, db.session, category='Direct DB Table Access'))
admin.add_view(ModelView(Attendance, db.session, category='Direct DB Table Access'))
admin.add_view(ModelView(RSVP, db.session, category='Direct DB Table Access'))
admin.add_view(ModelView(Project, db.session, category='Direct DB Table Access'))
admin.add_view(ModelView(ProjectMembership, db.session, category='Direct DB Table Access'))
