web: gunicorn app:app --log-file=-

init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade

#heroku run python manage.py db upgrade