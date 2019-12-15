import click
from flask.cli import with_appcontext

from app import db
from models import User

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
    click.echo("tables created!!!")
    #print("create_all was maked")

@click.command(name='create_admin')
@with_appcontext
def create_admin():
    #click.echo('Hello! Run command ok')
    nickname = "superadmin"
    admin = True
    u = User(nickname=nickname, admin=admin)
    #print("superadmin created", u)
    
    db.session.add(u)
    db.session.commit()
    click.echo("superadmin created!!!")

#Heroku $ flask create_all


if __name__ == '__main__':
	pass
	create_tables()
	create_admin()
