# URL Shortener (Django + DRF + PostgreSQL + Docker)

## 🚀 Starting a project
Install the latest version of [Python](https://www.python.org/downloads/)
   - I used the Python 3.13

### 1. Clone 
```
$  git clone https://github.com/leksus1966/djangoZipLink.git 
```
or
```
$  git clone git@github.com:leksus1966/djangoZipLink.git
```
**Enter the project directory**
```
$  cd djangoZipLink
```

**Activate Virtual Environment.**

For Windows
```
$  source venv/scripts/activate
```

For Linux and Mac
```
$  source .venv/bin/activate
```

**Install packages**
```
$ python3 -m pip install -r requirements.txt
```
**Install PostgreSQL and create database `shortener_db`**
```bash
$ psql -U postgres
postgres# CREATE DATABASE shortener_db;
```

**Apply migrations**
```
$ python3 manage.py migrate
```
### 2. Now Run the App
```
$ python manage.py runserver 0.0.0.0:8000
```
### 3. How to start in containers
```bash
docker-compose build
```
Starting.
```bash
docker-compose up
```

After starting:
- Django is available at: [http://localhost:8000](http://localhost:8000)
- API is available at: [http://localhost:8000/api/](http://localhost:8000/api/)

---

## 🛠 Using the API

### Create a short link
```bash
curl -X POST http://127.0.0.1:8000/api/create/ -H "Content-Type: application/json" -d '{"original_url": "https://google.com"}'
```

Response example:
```json
{
"id": 1,
"original_url": "https://google.com",
"short_code": "aB3dX9",
"created_at": "2025-09-07T12:00:00Z"
}
```

### Follow a short link
Open in browser:
```
http://127.0.0.1:8000/api/<short_code>/
```
### You will be redirected to the real link.

---

## 📦 Tech stack
- Python 3.13
- Django 5.2.6
- Django REST Framework 3.16.1
- PostgreSQL 16.9
- Docker + docker-compose

---

## 🗄 Connecting to PostgreSQL inside a container

By default, the `db` service with PostgreSQL 16 is enabled in docker-compose.

### Access to the database:
- **Host:** localhost
- **Port:** 5432
- **Database:** shortener_db
- **User:** postgres
- **Password:** postgres
---
- I included the `entrypoint.sh` script to ensure the Postgres db is ready to receive connections.
This is very important for running the application via docker-compose.

### Connecting via psql (locally):
```bash
psql -h localhost -p 5432 -U postgres -d shortener_db
```

### Connecting inside the container:
```bash
docker exec -it postgres_db psql -U postgres -d shortener_db
```

## Connect with me

- Github [https://github.com/leksus1966]
- Linkedin [https://www.linkedin.com/in/oleksii-sokalo-97589393/]