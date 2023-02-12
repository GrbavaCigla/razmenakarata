FROM python:3.11-alpine

WORKDIR /app

COPY ./backend/ .

# Packages
RUN pip3 install -U pip
RUN pip3 install -r requirements.txt

# Entry points
COPY ./docker/backend ./docker
RUN chmod +x ./docker/server-entrypoint.sh
RUN chmod +x ./docker/worker-entrypoint.sh
