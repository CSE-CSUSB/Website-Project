from models.user import User
from loader import bcrypt
from functools import wraps
from flask import session

class Auth:
    @staticmethod
    def check(username, password):
        user = User.query.filter_by(username=username).first()

        if user is not None and bcrypt.check_password_hash(user.password, password):
            return True

        return False

    @staticmethod
    def login(username, password):
        user = User.query.filter_by(username=username).first()

        if user is not None and bcrypt.check_password_hash(user.password, password):
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
