from loader import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer, unique=True)

    password = db.Column(db.Text)

    fname = db.Column(db.Text)
    lname = db.Column(db.Text)

    email_primary = db.Column(db.Text, unique=True)
    email_csusb = db.Column(db.Text, unique=True)

    standing = db.Column(db.Text)

    gender = db.Column(db.Text)

    shirt_size = db.Column(db.Text)
    shirt_received = db.Column(db.DateTime(timezone=True))

    majors = db.Column(db.Text)
    minors = db.Column(db.Text)

    paid_until = db.Column(db.DateTime(timezone=True))

    created = db.Column(db.DateTime(timezone=True))

    role = db.Column(db.Integer)
