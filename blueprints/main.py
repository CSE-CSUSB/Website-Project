from flask import Blueprint, render_template

blueprint = Blueprint('index', __name__)

@blueprint.route('/')
def index():
	#The main blueprint should not be hard-coded to load a site's blog. What if a site chooses not to have a blog?
    return render_template('blog.html', hideback=True)
    #return render_template('index.html', hideback=True)