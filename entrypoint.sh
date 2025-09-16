#!/bin/sh

echo "⏳ Waiting for Postgres ($DB_HOST:$DB_PORT)..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.5
done

echo "✅ Postgres is ready! I'm running migrations..."
python manage.py migrate

echo "🚀 Start Django..."
python manage.py runserver 0.0.0.0:8000