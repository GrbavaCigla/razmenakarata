#!/bin/sh

. "$PWD/.env"

# TODO: Add environment variable for redis port

while ! nc -z redis 6379; do echo "Waiting for redis:6379"; sleep 1; done