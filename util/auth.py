from models.user import User
from functools import wraps
from flask import session, redirect, url_for
import scrypt, base64, random, re

class Auth:
    @staticmethod
    def check(username, password):
        user = User.query.filter_by(username=username).first()

        if user is not None and (password == user.password):
            return True

        return False

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()

        if user is not None and (password == user.password):
            session['user'] = user

        return

    @staticmethod
    def logout():
        session.destroy()

    @staticmethod
    def hash_password(password):
        salt = base64.b64encode((''.join(chr(random.randint(0,255)) for i in range(32))).encode('utf-8'))
        hash = base64.b64encode(scrypt.hash(password, salt))
        return b''.join([b'$', salt, b'$', hash])

    def verify_password(hash, password):
        salt, hash = re.split(b'\$', hash)[1:]
        if scrypt.hash(password, salt) == base64.b64decode(hash):
            return True

        return False

def loggedin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session['user']:
            return redirect(url_for('.index'))

        return f(*args, **kwargs)

    return decorated_function
