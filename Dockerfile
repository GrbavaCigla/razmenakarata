FROM debian:bookworm

WORKDIR /app

RUN apt update && apt install nodejs npm python3 python3-pip tree netcat-traditional postgresql-client -y

# Python dependencies
# TODO: Use poetry env
COPY ./backend/requirements.txt backend/requirements.txt
RUN pip install -r backend/requirements.txt --break-system-packages

# Nodejs dependencies
COPY ./frontend/package.json frontend/package.json
COPY ./frontend/package-lock.json frontend/package-lock.json
RUN cd frontend && npm ci

COPY . .

EXPOSE 8000
