#!/bin/sh

sh "$PWD/docker/wait/db.sh"

cd backend/
python3 manage.py migrate || exit 1
# python manage.py migrate || exit 1