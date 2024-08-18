#!/bin/sh

. "$PWD/.env"

# TODO: Add environment variable for django port

while ! nc -z django 8000; do echo "Waiting for django:8000"; sleep 1; done