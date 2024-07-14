#!/bin/sh

sh "$PWD/docker/wait/db.sh"
sh "$PWD/docker/wait/redis.sh"
sh "$PWD/docker/wait/django.sh"

cd backend
REDIS_HOST=redis python3 manage.py runcelery