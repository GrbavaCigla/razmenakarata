FROM python:3.11.2-alpine

ENV WORKDIR /app

RUN mkdir $WORKDIR
WORKDIR $WORKDIR

# Frontend
ADD ./frontend/ $WORKDIR/frontend
RUN cd frontend && npm install
RUN cd frontend && npm run build --production

# Entry points
ADD ./docker/ $WORKDIR/docker
RUN chmod +x $WORKDIR/docker/frontend-entrypoint.sh
