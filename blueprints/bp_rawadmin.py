from datetime import datetime

from loader import db

from flask import Blueprint, render_template, redirect, url_for, session, flash, abort

from models import Club, Content, Member
from forms.pages import EditPageForm, DelPageForm
from sqlalchemy import desc, asc

from util.auth import Auth

blueprint = Blueprint('bp_rawadmin', __name__, url_prefix='/rawadmin')

@blueprint.before_request
def check_auth():
    if not 'user' in session:
        return redirect('/login')

    if session['user'].priv_level >= Auth.member:
        return redirect('/members')

@blueprint.route('/')
def view_database():
    tables = get_table_list()
    for t in tables:
        if t.name == 'club':
            return redirect(blueprint.url_prefix + '/table/club')
    return render_template('admin/rawadmin-db.html', tables=tables)

@blueprint.route('/table/<table>')
def view_table(table):
    tables = get_table_list()
    for t in tables:
        if t.name == table:
            activetable = t

            columns = activetable.c
            tharea = '<tr><th><input type="checkbox" name="rowtoggle" class="action-rowtoggle" title="Select all records" /></th>'
            for c in activetable.c:
                tharea = tharea + '<th><a href="#">' + c.name + '</a></th>'
            tharea = tharea + '</tr>'

            results = db.session.query(activetable)
            print(results.count())
            print(results)
            if results.count()==0:
                res = ['<tr><td>No results</td></tr>']
            else:
                res = []
                for r in results:
                    row = '<tr><td><input type="checkbox" name="rowid" class="action-checkbox" value="' + str(r.id) + '" title="Select record" /></td>'
                    for c in r:
                        row = row + '<td>' + str(c) + '</td>'
                    res.append(row + '</tr>')
            return render_template('admin/rawadmin-rawtable.html', tables=tables, activetable=activetable, columns=tharea, results=res, count=results.count())
    abort(404)

def get_table_list():
    tl = []
    for t in db.get_tables_for_bind():
        if t.name != "sessions":
            tl.append(t)
    tl.sort(key=lambda x: x.name)
    return tl