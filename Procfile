release: python manage.py migrate
web: gunicorn blog.wsgi
heroku ps:scale web=1