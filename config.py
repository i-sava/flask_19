# config.py
import os

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + os.path.join(basedir, 'app.db')
SECRET_KEY = os.environ.get('SECRET_KEY') or \
                          'secretsecret'
SQLALCHEMY_TRACK_MODIFICATIONS = True

APP_SETTINGS = "config.DevelopmentConfig"

