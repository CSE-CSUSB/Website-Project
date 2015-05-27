import os

from flask import Blueprint, render_template, abort, redirect
from util.auth import Auth

from util.template import get_admin, get_loggedin

import jinja2

from models import Content

from CommonMark.CommonMark import DocParser, HTMLRenderer

blueprint = Blueprint('bp_content', __name__)

@blueprint.route('/', defaults={'path': 'index'})
@blueprint.route('/<path:path>')
def content(path):
    #Temporarily, hard-code the main page (THIS MUST BE REMOVED FOR PRODUCTION USE)
    if path == 'index':
        try:
            return render_template('index.html')
        except jinja2.exceptions.TemplateNotFound:
            pass

    print("Querying the content table for url='" + path + "'")
    item = Content.query.filter_by(url=path).first()

    if not item:
        abort(404)

    if item.required_priv_level == Auth.permission_member and not get_loggedin():
        return redirect('/login')

    if item.required_priv_level == Auth.permission_admin and not get_admin():
        return redirect('/members')

    parser = DocParser()
    ast = parser.parse(item.data_blob)

    renderer = HTMLRenderer()

    if item.required_priv_level == Auth.permission_admin:
        return render_template('admin/admin.html', content=renderer.render(ast), title=item.title)

    if item.required_priv_level == Auth.permission_member:
        return render_template('members/members.html', content=renderer.render(ast), title=item.title)

    return render_template('page-sidebar.html', content=renderer.render(ast), title=item.title)
