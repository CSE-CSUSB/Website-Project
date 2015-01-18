from datetime import datetime

from loader import db

from flask import Blueprint, render_template, abort, redirect, session

from models.content import Content
from forms.editpage import EditPageForm
from forms.delpage import DelPageForm

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

@blueprint.route('/admin/')
@loggedin
def view_dashboard():
    return render_template('admin/view_dashboard.html')

@blueprint.route('/admin/content')
@loggedin
def view_pages():
    pages = Content.query.all()

    return render_template('admin/content/view_pages.html', pages=pages)

@blueprint.route('/admin/content/add', methods=['GET', 'POST'])
@loggedin
def add_page():
    form = EditPageForm()

    if form.validate_on_submit():
        page = Content()
        page.title = form.title.data
        page.url = form.url.data.lower()
        page.content = form.content.data
        page.created_by = session['user'].id
        page.created_on = datetime.now()
        page.edited_by = 0
        page.edited_on = datetime.now()

        db.session.add(page)
        db.session.commit()

        return redirect('/admin/content')

    return render_template('admin/content/edit_page.html', action='Create New', title='Create Page', form=form)

@blueprint.route('/admin/content/edit/<id>', methods=['GET', 'POST'])
@loggedin
def edit_page(id):
    page = Content.query.get(id)

    if not page:
        return redirect('/admin/content')

    form = EditPageForm()

    if form.validate_on_submit():
        page.title = form.title.data
        page.url = form.url.data
        page.content = form.content.data
        page.edited_by = session['user'].id
        page.edited_on = datetime.now()

        db.session.merge(page)
        db.session.commit()

        return redirect('/admin/content')

    else:
        form.title.data = page.title
        form.url.data = page.url
        form.content.data = page.content

    return render_template('admin/content/edit_page.html', action='Edit', title='Edit Page', form=form)

@blueprint.route('/admin/content/delete/<id>', methods=['GET', 'POST'])
@loggedin
def delete_page(id):
    page = Content.query.get(id)

    if not page:
        return redirect('/admin/content')

    form = DelPageForm()

    if form.validate_on_submit():
        db.session.delete(page)
        db.session.commit()

        return redirect('/admin/content')

    return render_template('admin/content/delete_page.html', title='Delete Page', page=page, form=form)