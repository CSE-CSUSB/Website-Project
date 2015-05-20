from loader import db

# For reference:
# http://docs.sqlalchemy.org/en/latest/core/metadata.html
# http://docs.sqlalchemy.org/en/latest/core/type_basics.html
# http://docs.sqlalchemy.org/en/latest/dialects/postgresql.html
# http://www.pythoncentral.io/sqlalchemy-orm-examples/

'''
# This table is already defined by util.sessions.py, but this is what it looks like
class Sessions(db.Model):
    __tablename__ = 'sessions'
    key                     = db.Column(db.String(length=250), nullable=False, primary_key=True)
    value                   = db.Column(db.LargeBinary, nullable=False)
'''
class Club(db.Model):
    __tablename__ = 'club'
    id                      = db.Column(db.Integer, primary_key=True)       # SQLAlchemy will make this a SERIAL type (see reference above)
    shortname               = db.Column(db.Text, nullable=False)
    longname                = db.Column(db.Text, nullable=False)

class Member(db.Model):
    __tablename__ = 'member'
    id                      = db.Column(db.Integer, primary_key=True)       # SQLAlchemy will make this a SERIAL type (see reference above)
    student_id              = db.Column(db.CHAR(length=9), unique=True)
    primary_club            = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)
    assigned_team           = db.Column(db.Integer)
    priv_level              = db.Column(db.Integer, nullable=False)         # -2 officer, -1 admin, 0 member, 1 alumni, 2 associate
    pw_hash                 = db.Column(db.Text)
    pin_hash                = db.Column(db.Text)
    name_first              = db.Column(db.Text, nullable=False)
    name_middle             = db.Column(db.Text, nullable=False)
    name_last               = db.Column(db.Text, nullable=False)
    phone                   = db.Column(db.Text)
    Texting_ok              = db.Column(db.Boolean)
    email1                  = db.Column(db.Text, unique=True, nullable=False)
    email2                  = db.Column(db.Text, unique=True)
    picture                 = db.Column(db.Text)
    gender                  = db.Column(db.Text)
    acad_standing           = db.Column(db.Text)
    acad_major              = db.Column(db.Text)
    acad_minor              = db.Column(db.Text)
    acad_conc               = db.Column(db.Text)
    acad_grad_qtr           = db.Column(db.Text)
    signup_date             = db.Column(db.DateTime(timezone=False), nullable=False)
    paid_amount             = db.Column(db.Numeric(precision=5, scale=2))
    paid_date               = db.Column(db.DateTime(timezone=False))
    paid_until_date         = db.Column(db.DateTime(timezone=False))
    receipt_date            = db.Column(db.DateTime(timezone=False))
    badge_type              = db.Column(db.Integer)
    shirt_size              = db.Column(db.Text)
    shirt_received_date     = db.Column(db.DateTime(timezone=False))

class Content(db.Model):
    __tablename__ = 'content'
    id                      = db.Column(db.Integer, primary_key=True)       # SQLAlchemy will make this a SERIAL type (see reference above)
    content_type            = db.Column(db.Text, nullable=False)
    url                     = db.Column(db.Text, unique=True)
    title                   = db.Column(db.Text)
    created_on              = db.Column(db.DateTime(timezone=True))
    created_by              = db.Column(db.Integer, db.ForeignKey('member.id'))
    edited_on               = db.Column(db.DateTime(timezone=True))
    edited_by               = db.Column(db.Integer, db.ForeignKey('member.id'))
    required_priv_level     = db.Column(db.Integer)                         # 2 = officer, 1 = member, 0 = public
    show_in_nav             = db.Column(db.Boolean)                         # yes or no, will show in the nav of the lowest group its available to
    data_blob               = db.Column(db.Text, nullable=False)

class Event(db.Model):
    __tablename__ = 'event'
    id                      = db.Column(db.Integer, primary_key=True)       # SQLAlchemy will make this a SERIAL type (see reference above)
    title                   = db.Column(db.Text, nullable=False)
    hosting_club            = db.Column(db.Integer, db.ForeignKey('club.id'))
    presenter               = db.Column(db.Text)
    picture                 = db.Column(db.Text)
    shorturl                = db.Column(db.Text, unique=True)
    start_time              = db.Column(db.DateTime(timezone=True))
    end_time                = db.Column(db.DateTime(timezone=True))
    location                = db.Column(db.Text)
    location_type           = db.Column(db.Integer)
    contact_info            = db.Column(db.Text)
    content_block_id        = db.Column(db.Integer, db.ForeignKey('content.id'))
    rsvp_max_replies        = db.Column(db.Integer)
    rsvp_allow_maybe        = db.Column(db.Boolean, nullable=False)
    rsvp_allow_comments     = db.Column(db.Boolean, nullable=False)
    rsvp_public_view        = db.Column(db.Boolean, nullable=False)
    rsvp_send_reminder      = db.Column(db.Boolean, nullable=False)

class Attendance(db.Model):
    __tablename__ = 'attendance'
    id                      = db.Column(db.Integer, primary_key=True)       # SQLAlchemy will make this a SERIAL type (see reference above)
    member                  = db.Column(db.Integer, db.ForeignKey('member.id'))
    event                   = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    comment                 = db.Column(db.Text)

class RSVP(db.Model):
    __tablename__ = 'rsvp'
    id                      = db.Column(db.Integer, primary_key=True)       # SQLAlchemy will make this a SERIAL type (see reference above)
    member                  = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    event                   = db.Column(db.Integer, db.ForeignKey('event.id'), nullable=False)
    reply                   = db.Column(db.Integer, nullable=False)         #0 No, 1 Yes, 2 Maybe
    comment                 = db.Column(db.Text)

class Project(db.Model):
    __tablename__ = 'project'
    id                      = db.Column(db.Integer, primary_key=True)       # SQLAlchemy will make this a SERIAL type (see reference above)
    title                   = db.Column(db.Text, nullable=False)
    content_block_id        = db.Column(db.Integer, db.ForeignKey('content.id'))
    leader                  = db.Column(db.Integer, db.ForeignKey('member.id'))

class ProjectMembership(db.Model):
    __tablename__ = 'projectmembership'
    project                 = db.Column(db.Integer, db.ForeignKey('project.id'), primary_key=True)
    member                  = db.Column(db.Integer, db.ForeignKey('member.id'), primary_key=True)
    add_date                = db.Column(db.DateTime(timezone=True))
