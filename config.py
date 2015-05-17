class Config:
    # Change all of these for non-development situations
    DEBUG = True      #Strangely, enabling this causes the Flask server to reload immediately after the first load finishes
    SECRET_KEY = '1234567890'
    ENCRYPTION_TIME = 0.025

    SQLALCHEMY_DATABASE_URI = 'postgresql://csecw:csecw@127.0.0.1/csecw'
