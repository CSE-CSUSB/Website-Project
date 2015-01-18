import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt

from config import Config

from util.session import KVSessionInterface, KVSessionExtension
from simplekv.db.sql import SQLAlchemyStore

from flask import session
import util.template

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
sessionStore = SQLAlchemyStore(db.engine, db.metadata, 'sessions')
KVSessionExtension(sessionStore, app)
bcrypt = Bcrypt(app)

app.basepath = '/'.join(os.path.realpath(__file__).split("/")[:-1]) + '/'

for root, dirs, files in os.walk(app.basepath + 'blueprints'):
    for name in [n for n in files if "__init__.py" not in n and n.endswith(".py")]:
        n = os.path.join(root, name)[:-3].replace(app.basepath, '').replace('/', '.')
        module, attr = n.rsplit('.', 1)
        imp = __import__(module, fromlist=[attr])
        attr = getattr(imp, attr)
        if hasattr(attr, 'blueprint'):
            app.register_blueprint(attr.blueprint)