from flask import Blueprint, render_template, abort, redirect
from util.auth import Auth

from util.template import get_admin, get_loggedin

from models.content import Content

from CommonMark.CommonMark import DocParser, HTMLRenderer

blueprint = Blueprint('content', __name__)

@blueprint.route('/', defaults={'path': 'index'})
@blueprint.route('/<path:path>')
def content(path):
    item = Content.query.filter_by(url=path).first()

    if not item:
        abort(404)

    if item.require_level == Auth.permission_member and not get_loggedin():
        return redirect('/login')

    if item.require_level == Auth.permission_admin and not get_admin():
        return redirect('/members')

    parser = DocParser()
    ast = parser.parse(item.content)

    renderer = HTMLRenderer()

    if item.require_level == Auth.permission_admin:
        return render_template('admin/admin.html', content=renderer.render(ast), title=item.title)

    if item.require_level == Auth.permission_member:
        return render_template('members/members.html', content=renderer.render(ast), title=item.title)

    return render_template('page.html', content=renderer.render(ast), title=item.title)
