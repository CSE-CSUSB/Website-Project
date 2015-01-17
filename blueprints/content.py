from flask import Blueprint, render_template, abort

from models.content import Content

from CommonMark.CommonMark import DocParser, HTMLRenderer

blueprint = Blueprint('content', __name__)

@blueprint.route('/', defaults={'path': 'index'})
@blueprint.route('/<path:path>')
def content(path):
    item = Content.query.filter_by(url=path).first()

    if not item:
       abort(404)

    parser = DocParser()
    ast = parser.parse(item.content)

    renderer = HTMLRenderer()

    return render_template('content.html', content=renderer.render(ast))