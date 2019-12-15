import click
from flask.cli import with_appcontext

from app import db
from models import User

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    print("create_all was maked")

@click.command(name='create_admin')
@with_appcontext
def create_admin():
    click.echo('Hello! Run command ok')
    nickname = "superadmin"
    admin = True
    u = User(nickname=nickname, admin=admin)
    print("superadmin created", u)
    db.session.add(u)
    db.session.commit() 

#Heroku $ flask create_all

'''
if __name__ == '__main__':
	pass
	db.create_all()
	create_admin()
'''