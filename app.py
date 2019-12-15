from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config.from_pyfile(config_file = 'config.py')
app.config.from_object('config')

db = SQLAlchemy(app)

from routes import hello

if __name__ == '__main__':
    app.run()
