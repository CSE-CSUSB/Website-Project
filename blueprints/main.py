from flask import Blueprint, render_template

from forms.login import LoginForm

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
def index():
    form = LoginForm()

    return render_template('login.html', form=form)