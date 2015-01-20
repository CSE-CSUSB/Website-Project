from loader import db


class Content(db.Model):
    __tablename__ = 'content'

    id = db.Column(db.Integer, primary_key=True)

    url = db.Column(db.Text, unique=True)

    title = db.Column(db.Text)

    created_by = db.Column(db.Integer)
    created_on = db.Column(db.DateTime(timezone=True))

    edited_by = db.Column(db.Integer)
    edited_on = db.Column(db.DateTime(timezone=True))

    content = db.Column(db.Text)

    # null if not at all, otherwise negative for admin, 0+ for members
    require_level = db.Column(db.Boolean)

    # 0 for not at all, 1 for main page, 2 for members area, 3 for admin area
    in_navigation = db.Column(db.Integer)