#! /bin/bash

#set -e
python /code/manage.py collectstatic --noinput

gunicorn -c /code/gunicorn-conf.py --bind 0.0.0.0:$GUNICORN_PORT --chdir gyser gyser.wsgi:application
