from datetime import datetime

from loader import app

@app.template_global()
def get_year():
    return datetime.now().year