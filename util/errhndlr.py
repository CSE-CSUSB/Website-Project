from loader import app
from flask import render_template

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page.html', content="Error: page not found", title="404"), 404
