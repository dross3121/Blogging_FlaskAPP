import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
#Flask-SQLAlchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI configuration variable.
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
#set to false to not signal whenever there are new changes
    SQLALCHEMY_TRACK_MODIFICATIONS = False