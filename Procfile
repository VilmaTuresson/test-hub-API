release: python manage.py makemigrations && python manage.py migrate
web: gunicorn testhub_api.wsgi