from flask import Blueprint, render_template, abort, redirect

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

    if item.require_level == 1 and not get_loggedin():
        return redirect('/login')

    if item.require_level == 2 and not get_admin():
        return redirect('/members')

    parser = DocParser()
    ast = parser.parse(item.content)

    renderer = HTMLRenderer()

    return render_template('page.html', content=renderer.render(ast), title=item.title)
