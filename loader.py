import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from config import Config

from util.session import KVSessionInterface, KVSessionExtension
from simplekv.db.sql import SQLAlchemyStore

from flask import session

app = Flask(__name__)

# Load the config
# In the future, consider using an environment variable for this, so the code doesn't have to be changed
# See the suggestions in http://flask.pocoo.org/docs/0.10/config/
c = 'config.DevelopmentConfig'
print("Loading config '" + c + "'")
app.config.from_object(c)

print("Initializing SQLAlchemy")
db = SQLAlchemy(app)

print("Initializing sessions")
sessionStore = SQLAlchemyStore(db.engine, db.metadata, 'sessions')
KVSessionExtension(sessionStore, app)

app.basepath = '/'.join(os.path.realpath(__file__).split("/")[:-1]) + '/'

print("Loading modules...")
for root, dirs, files in os.walk(app.basepath + 'blueprints'):
    for name in [n for n in files if "__init__.py" not in n and n.endswith(".py")]:
        n = os.path.join(root, name)[:-3].replace(app.basepath, '').replace('/', '.')
        module, attr = n.rsplit('.', 1)
        print(" - Importing " + module + "/" + attr)
        imp = __import__(module, fromlist=[attr])
        attr = getattr(imp, attr)
        if hasattr(attr, 'blueprint'):
            print("     " + "done.")
            app.register_blueprint(attr.blueprint)

import util.template
