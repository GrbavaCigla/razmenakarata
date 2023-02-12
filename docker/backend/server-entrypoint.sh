#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
# python manage.py createsuperuser --noinput
gunicorn razmenakarata.wsgi --bind 0.0.0.0:8000 --workers 4 --threads 4