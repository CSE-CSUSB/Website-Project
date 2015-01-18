class Config:
    # Change all of these for non-development situations
    DEBUG = True
    SECRET_KEY = '1234567890'
    ENCRYPTION_TIME = 0.025

    SQLALCHEMY_DATABASE_URI = 'postgresql://csecw:csecw@cse-club.com/csecw'
