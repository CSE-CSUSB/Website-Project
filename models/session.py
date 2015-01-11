from loader import db


class Session(db.Model):
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.Text, unique=True)

    user = db.Column(db.Integer)

    ip = db.Column(db.Text)

    start = db.Column(db.DateTime(timezone=True))

    active = db.Column(db.DateTime(timezone=True))

    valid = db.Column(db.Boolean)
