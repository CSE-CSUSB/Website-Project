from datetime import datetime

from loader import db

from flask import Blueprint, render_template, abort, redirect, session

from models.content import Content
from forms.addpage import AddPageForm

from CommonMark.CommonMark import DocParser, HTMLRenderer
from util.auth import loggedin

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

    return render_template('content.html', content=renderer.render(ast), title=item.title)


@blueprint.route('/admin/content')
def view_pages():
    pages = Content.query.all()

    return render_template('admin/view_pages.html', pages=pages)

@loggedin
@blueprint.route('/admin/content/add', methods=['GET', 'POST'])
def add_page():
    form = AddPageForm()

    if form.validate_on_submit():
        print(session['user'])
        page = Content()
        page.title = form.title.data
        page.url = form.url.data
        page.content = form.content.data
        page.created_by = session['user']
        page.created_on = datetime.now()
        page.edited_by = 0
        page.edited_on = datetime.now()

        db.session.add(page)
        db.session.commit()

        return redirect('/admin/content')

    return render_template('admin/add_page.html', action='Create New', title='Create Page', form=form)


@blueprint.route('/admin/content/edit/<id>')
def edit_page(id):
    return


@blueprint.route('/admin/content/delete/<id>')
def delete_page(id):
    return