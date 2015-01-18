from models.user import User
from functools import wraps
from flask import session
import scrypt

class Auth:
    @staticmethod
    def check(username, password):
        user = User.query.filter_by(username=username).first()

        if user is not None and (password == scrypt.hash(user.password, user.salt)):
            return True

        return False

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()

        if user is not None and (password == scrypt.hash(user.password, user.salt)):
            session["username"] = username;

        return

    @staticmethod
    def logout():
        session.destroy()


def loggedin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session["username"]:
            return redirect(url_for('.index'))

        return f(*args, **kwargs)

    return decorated_function
