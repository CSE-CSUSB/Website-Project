from models.user import User
from flask import session
import scrypt, base64, random, re
from sqlalchemy import or_


class Auth:

    # role constants
    officer = -2
    admin = -1
    member = 0
    alumni = 1
    associate = 2

    @staticmethod
    def check(id, password):
        if id.isdigit():
            user = User.query.filter_by(cid=id).first()
        else:
            user = User.query.filter(or_(User.email_primary==id, User.email_csusb==id)).first()

        if user is not None and Auth.verify_password(password, user.password):
            return True

        return False

    @staticmethod
    def login(id, password):
        if id.isdigit():
            user = User.query.filter_by(cid=id).first()
        else:
            user = User.query.filter(or_(User.email_primary==id, User.email_csusb==id)).first()

        if user is not None and Auth.verify_password(password, user.password):
            session['user'] = user

        return

    @staticmethod
    def logout():
        session.destroy()

    @staticmethod
    def hash_password(password):
        salt = base64.b64encode((''.join(chr(random.randint(0, 255)) for i in range(32))).encode('utf-8'))
        hash = base64.b64encode(scrypt.hash(password, salt))
        return (b''.join([b'$', salt, b'$', hash])).decode('ascii')

    @staticmethod
    def verify_password(password, hash):
        salt, hash = re.split(b'\$', hash.encode('utf-8'))[1:]
        if scrypt.hash(password, salt) == base64.b64decode(hash):
            return True

        return False
