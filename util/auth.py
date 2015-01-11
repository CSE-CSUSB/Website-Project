from models.user import User

from util.session import Session

from loader import bcrypt


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
            Session.create(user)

        return

    @staticmethod
    def logout():
        Session.destroy()

