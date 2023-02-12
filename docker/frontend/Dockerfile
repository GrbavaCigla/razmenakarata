FROM node:19.6-alpine

WORKDIR /app

# Packages
COPY ./frontend/ .
RUN npm install
RUN npm run build --production

# Entry points
COPY ./docker/frontend ./docker
RUN chmod +x ./docker/frontend-entrypoint.sh
