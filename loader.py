import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from util.session import KVSessionInterface, KVSessionExtension
from simplekv.db.sql import SQLAlchemyStore

from flask import session

print("\nInitializing Flask using __name__ = '" + __name__ + "'")
app = Flask(__name__, static_url_path='/static', static_folder='static-infosec', template_folder='templates-infosec')
#app = Flask(__name__)

# Load the config
# In the future, consider using an environment variable for this, so the code doesn't have to be changed
# See the suggestions in http://flask.pocoo.org/docs/0.10/config/
c = 'config.DevelopmentConfig'
print("Config = '" + c + "'")
app.config.from_object(c)

print("Initializing SQLAlchemy")
db = SQLAlchemy(app)

print("Initializing sessions")
sessionStore = SQLAlchemyStore(db.engine, db.metadata, 'sessions')
KVSessionExtension(sessionStore, app)

# Is there any way we can put these into app.config ?
BLUEPRINTS_ENABLED = ['bp_auth','bp_content','bp_members','bp_rawadmin']

print("Loading blueprints..." + str(BLUEPRINTS_ENABLED))
bpdir = 'blueprints'
for m in BLUEPRINTS_ENABLED:
    # Check if file exists
    if os.path.exists(bpdir + '/' + m + '.py'):
        # Perform low-level python import
        imp = __import__(bpdir, fromlist=[m])
        # Get a referenc to the blueprint variable that should be defined in each file
        attr = getattr(imp, m)
        if hasattr(attr, 'blueprint'):
            # Register the blueprint with Flask
            app.register_blueprint(attr.blueprint)
    else:
        print('Cannot find blue print \'' + m + '\'')

# What in the world does this chunk of code do? If we keep it, it needs comments.
'''app.basepath = '/'.join(os.path.realpath(__file__).split("/")[:-1]) + '/'
for root, dirs, files in os.walk(app.basepath + 'blueprints'):
    for name in [n for n in files if "__init__.py" not in n and n.endswith(".py")]:
        n = os.path.join(root, name)[:-3].replace(app.basepath, '').replace('/', '.')
        module, attr = n.rsplit('.', 1)
        print(" " + module + "/" + attr)
        imp = __import__(module, fromlist=[attr])
        attr = getattr(imp, attr)
        if hasattr(attr, 'blueprint'):
            app.register_blueprint(attr.blueprint)'''

if app.config['DEBUG']:
    print("Enabled routes...")
    for u in app.url_map.iter_rules():
        print(" " + str(u.rule) + " -> " + str(u.endpoint))
    print ('\n------------\n\n\n\n')

import util.template
import util.errhndlr
