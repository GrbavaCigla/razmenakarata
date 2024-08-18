#!/bin/sh

sh "$PWD/docker/wait/db.sh"
sh "$PWD/docker/wait/redis.sh"

cd backend/
REDIS_HOST=redis python3 manage.py runserver 0.0.0.0:8000