class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'

# Environment used on each developer's local machine for working on new code
class DevelopmentConfig(Config):
    DEBUG = True      #Strangely, enabling this causes the Flask server to reload immediately after the first load finishes
    TESTING = True
    SECRET_KEY = '1234567890'
    ENCRYPTION_TIME = 0.025
    SQLALCHEMY_DATABASE_URI = 'postgresql://dev:password@127.0.0.1/clubsitedev'

# An environment as similar to the production environment as possible, without actually being live to the world
class StagingConfig(Config):
    SECRET_KEY = 'THIS_MUST_BE_CHANGED'
    ENCRYPTION_TIME = 0.025
    SQLALCHEMY_DATABASE_URI = 'postgresql://staging:staging@127.0.0.1/staging'

# The real website
class ProductionConfig(Config):
    SECRET_KEY = 'THIS_MUST_BE_CHANGED'
    ENCRYPTION_TIME = 0.025
    SQLALCHEMY_DATABASE_URI = 'postgresql://csecw:csecw@127.0.0.1/csecw'
