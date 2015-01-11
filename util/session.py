from random import randrange
from datetime import datetime, timedelta
from functools import wraps

from flask import request, session, redirect, url_for

from models.session import Session as SessionModel
from models.user import User
from loader import db


class Session:
    @staticmethod
    def create(user):
        old = SessionModel.query.filter_by(user=user.id).order_by(SessionModel.id.desc()).first()

        if old is not None:
            old.valid = False

        new = SessionModel(key=Session._generatekey(), user=user.id, ip=request.remote_addr, start=datetime.utcnow(),
                           active=datetime.utcnow(), valid=True)

        db.session.add(new)
        db.session.commit()

        session['key'] = new.key

        return

    @staticmethod
    def destroy():
        session.pop('key', None)

        return

    @staticmethod
    def check():
        sess = Session._get()

        if sess is None or sess.valid is not True:
            return False

        if sess.active < datetime.utcnow() - timedelta(minutes=30) or sess.ip != request.remote_addr:
            sess.valid = False

            db.session.commit()

            return False

        Session._refresh()

        return True

    @staticmethod
    def user():
        sess = Session._get()
        return User.query.get(sess.user)

    @staticmethod
    def _get():
        return SessionModel.query.filter_by(key=session.get('key', None)).first()

    @staticmethod
    def _refresh():
        sess = Session._get()
        sess.active = datetime.utcnow()

        db.session.commit()

        return

    @staticmethod
    def _generatekey():
        key = "%032x" % randrange(16 ** 32)

        if SessionModel.query.filter_by(key=key).first() is not None:
            return Session._generatekey()

        return key


def loggedin(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not Session.check():
            return redirect(url_for('.index'))

        return f(*args, **kwargs)

    return decorated_function

