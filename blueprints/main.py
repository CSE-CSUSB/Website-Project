from flask import Blueprint, render_template

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
def index():
    return render_template('page.html', content="Welcome to the CSE Club website! <a href=\"/login/\">Log in</a>", hideback=True)