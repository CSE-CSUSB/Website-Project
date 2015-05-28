from datetime import datetime
from loader import app, db
from models import *
from util.auth import Auth

def additem(table, item):
  if table.query.filter_by(id=item.id).first() is None:
    db.session.add(item)
    print('  ' + table.__tablename__ + ' id ' + str(item.id) + ' added')
  else:
    print('  ' + table.__tablename__ + ' id ' + str(item.id) + ' already exists')

if __name__ == '__main__':
  print('Adding sample clubs...')
  additem(Club,Club(id = 8001, shortname = "InfoSec",
                    longname = "Information Security Club"))
  additem(Club,Club(id = 8002, shortname = "ACM",
                    longname = "Association For Computing Machinery"))
  additem(Club,Club(id = 8003, shortname = "IEEE",
                    longname = "Institute of Electrical and Electronics Engineers"))

  print('Adding sample members, all with a password of \'password\'...')
  additem(Member,Member(id=5001, student_id = "000000001", pw_hash = Auth.hash_password('password'),
                        primary_club = 8002,
                        priv_level = Auth.admin,
                        name_first = "Mike", name_middle = "", name_last = "Korcha",
                        email1 = "mikekorcha@gmail.com", email2="korcham@coyote.csusb.edu",
                        acad_standing = "Graduate", gender="Male", shirt_size="M",
                        signup_date = datetime.utcfromtimestamp(0)))
  additem(Member,Member(id=5002, student_id = "000000002", pw_hash = Auth.hash_password('password'),
                        primary_club = 8001,
                        priv_level = Auth.member,
                        name_first = "Kenneth", name_middle = "", name_last = "Johnson",
                        email1 = "kenpilot@gmail.com",
                        acad_standing="Undergraduate",
                        signup_date = datetime.utcfromtimestamp(0)))

  print('Adding sample content blocks...')
  additem(Content,Content(id=901, content_type='html', url='index',
                          title='Home page', show_in_nav=1,
                          required_priv_level=Auth.permission_general,
                          data_blob='Home page content here'))
  additem(Content,Content(id=902, content_type='markdown', url='',
                          title='WRCCDC', show_in_nav=2,
                          required_priv_level=Auth.permission_general,
                          data_blob='# Western Regional Collegiate Cyber Defense Competition\n\n## About\n\nHosted by CalPoly Pomona.\n\n## How we practice for it\n\nIn a super cool lab.'))

  print('Adding sample events...')
  additem(Event,Event(id=201, title='Workshop #1',
                      hosting_club=Club.query.filter_by(shortname="InfoSec").first().id,
                      rsvp_allow_maybe=False, rsvp_allow_comments=False,
                      rsvp_public_view=True, rsvp_send_reminder=False))

  print('Adding sample RSVPs...')
  additem(RSVP,RSVP(id=101, member=5002, event=201,
                    reply=1, comment='See ya there!'))

  db.session.commit()
  print('Done.')
