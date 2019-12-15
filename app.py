from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# app.config.from_pyfile(config_file = 'config.py')
app.config.from_object('config')

db = SQLAlchemy(app)

from models import User

@app.route('/')
def hello():
    users = User.query.all()
    about = ''
    if users:
        for user in users:
            about += "<p>nickname and admin_role: </p>" + user.nickname + str(user.admin)
    return "<h1> Hello World! </h1>" + about

@app.route('/add/')
def webhook():
    nickname = "Admin"
    admin = True
    u = User(nickname=nickname, admin=admin)
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"



@app.route('/del/')
def delete():
    db.session.query(User).delete()
    db.session.commit()
    return "users del"


if __name__ == '__main__':
    app.run()
