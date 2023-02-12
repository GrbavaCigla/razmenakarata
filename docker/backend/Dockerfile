FROM python:3.11-alpine

ENV WORKDIR /app

RUN mkdir $WORKDIR
WORKDIR $WORKDIR

ADD ./backend/ $WORKDIR/backend

# Python
RUN pip3 install -U pip
RUN pip3 install -r backend/requirements.txt

# Entry points
ADD ./docker/ $WORKDIR/docker
RUN chmod +x $WORKDIR/docker/backend/server-entrypoint.sh
RUN chmod +x $WORKDIR/docker/backend/worker-entrypoint.sh
