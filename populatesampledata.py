from datetime import datetime
from loader import app, db
from models import *
from util.auth import Auth

if __name__ == '__main__':
    # Create sample data
    print('Adding sample clubs...')
    db.session.add(Club(shortname = "InfoSec",
                        longname = "Information Security Club"))
    db.session.add(Club(shortname = "ACM",
                        longname = "Association For Computing Machinery"))
    db.session.add(Club(shortname = "IEEE",
                        longname = "Institute of Electrical and Electronics Engineers"))

    print('Adding sample members, all with a password of \'password\'...')
    db.session.add(Member(student_id = "004457231", pw_hash = Auth.hash_password('password'),
                          club = Club.query.filter_by(shortname="InfoSec").first().id,
                          priv_level = 0, name_first = "Kenneth", name_middle = "", name_last = "Johnson",
                          email1 = "test@gmail.com",
                          acad_standing="Undergraduate",
                          signup_date = datetime.utcfromtimestamp(0)))
    db.session.add(Member(student_id = "003784312", pw_hash = Auth.hash_password('password'),
                          club = Club.query.filter_by(shortname="ACM").first().id,
                          priv_level = 0, name_first = "Mike", name_middle = "", name_last = "Korcha",
                          email1 = "mikekorcha@gmail.com", email2="korcham@coyote.csusb.edu",
                          acad_standing = "Graduate", gender="Male", shirt_size="M",
                          signup_date = datetime.utcfromtimestamp(0)))
    db.session.commit()

    print('Done.')
