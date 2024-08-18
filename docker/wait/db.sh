#!/bin/sh

. "$PWD/.env"

while ! nc -z db $POSTGRES_PORT; do echo "Waiting for db:$POSTGRES_PORT"; sleep 1; done
while ! echo 'SELECT 1' | PGPASSWORD=$POSTGRES_PASSWORD psql --host db --port $POSTGRES_PORT --user $POSTGRES_USER $POSTGRES_NAME; do echo "Waiting for DB"; sleep 1; done