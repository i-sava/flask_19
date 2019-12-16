from models import User
from app import app, db

@app.route('/')
def hello():
    users = User.query.all()
    about = ''
    if users:
        for user in users:
            about += "<p>nickname: " + user.nickname + "\t | admin_role: " + str(user.admin) + "</p>"
    return "<h1> Hello World! </h1>" + about

@app.route('/add/')
def webhook():
    nickname = "User_"
    admin = False
    u = User(nickname=nickname)
    print("user created", u)
    db.session.add(u)
    db.session.commit()
    return "user created"


@app.route('/del/')
def delete():
    db.session.query(User).delete()
    db.session.commit()
    return "users del"
