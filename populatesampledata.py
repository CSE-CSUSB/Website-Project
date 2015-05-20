from datetime import datetime
from loader import app, db
from models import *
from util.auth import Auth

if __name__ == '__main__':
    # Create sample data

    print('Adding sample clubs...')
    if (Club.query.filter_by(shortname="InfoSec").first() is None):
      db.session.add(Club(shortname = "InfoSec",
                        longname = "Information Security Club"))
    if (Club.query.filter_by(shortname="ACM").first() is None):
      db.session.add(Club(shortname = "ACM",
                        longname = "Association For Computing Machinery"))
    if (Club.query.filter_by(shortname="IEEE").first() is None):
      db.session.add(Club(shortname = "IEEE",
                        longname = "Institute of Electrical and Electronics Engineers"))

    print('Adding sample members, all with a password of \'password\'...')
    if (Member.query.filter_by(student_id = "000000001").first() is None):
      db.session.add(Member(student_id = "000000001", pw_hash = Auth.hash_password('password'),
                          primary_club = Club.query.filter_by(shortname="ACM").first().id,
                          priv_level = 0, name_first = "Mike", name_middle = "", name_last = "Korcha",
                          email1 = "mikekorcha@gmail.com", email2="korcham@coyote.csusb.edu",
                          acad_standing = "Graduate", gender="Male", shirt_size="M",
                          signup_date = datetime.utcfromtimestamp(0)))
    if (Member.query.filter_by(student_id = "000000002").first() is None):
      db.session.add(Member(student_id = "000000002", pw_hash = Auth.hash_password('password'),
                          primary_club = Club.query.filter_by(shortname="InfoSec").first().id,
                          priv_level = 0, name_first = "Kenneth", name_middle = "", name_last = "Johnson",
                          email1 = "test@gmail.com",
                          acad_standing="Undergraduate",
                          signup_date = datetime.utcfromtimestamp(0)))

    db.session.commit()
    print('Done.')
