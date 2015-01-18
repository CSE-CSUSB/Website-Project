from loader import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.Text, unique=True)
    password = db.Column(db.Text)

    email = db.Column(db.Text, unique=True)

    created = db.Column(db.DateTime(timezone=True))

    role = db.Column(db.Integer)
