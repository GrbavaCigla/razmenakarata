# RazmenaKarata
Platform to exchange concert/event tickets.

## Table of contents
1. [Installation](#installation)
    1. [Docker](#docker)
    2. [Manual](#manual)
        1. [Frontend](#frontend)
        2. [Backend](#backend)
            1. [Pipenv](#pipenv)
            1. [Manual](#manual-1)
2. [Usage](#usage-dev)
    1. [Backend](#backend-1)
    2. [Frontend](#frontend-1)
3. [License](#license)
## Installation

### Docker

Coming soon, docker branch currently WIP.

### Manual

Before installing project dependencies, make sure you have redis installed.

#### Frontend

Install npm dependencies:

```sh
cd frontend
npm install
```

#### Backend

There are two ways to install dependencies for backend

##### Pipenv

```sh
cd backend
pipenv install
```

##### Manual

```sh
cd backend
pip install -r requirements.txt
```

## Usage (Dev)
Again, docker configuration is not done yet...

To run with postgresql instead of sqlite, set `DJANGO_DB` to `postgres`.  
List of environment variables:
| Variable            | Default        |
|---------------------|----------------|
| `SECRET_KEY`        | random         |
| `POSTGRES_HOST`     | localhost      |
| `POSTGRES_NAME`     | postgres       |
| `POSTGRES_USER`     | postgres       |
| `POSTGRES_PASSWORD` | postgres       |
| `POSTGRES_PORT`     | 5432           |
| `DJANGO_DB`         | sqlite         |
| `REDIS_HOST`        | 127.0.0.1:6379 |

Before starting backend, start redis with `redis-server` command.
### Backend
```sh
cd backend
python manage.py runserver
```
Background worker:
``` sh
python manage.py run_huey
```
### Frontend
```sh
cd frontend
npm run dev
```

## License
Project is licensed under [GPLv3](https://github.com/GrbavaCigla/razmenakarata/blob/master/LICENSE) license.
