#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Apply database migrations
echo "Making and applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
echo "Starting Django development server..."
exec python manage.py runserver 0.0.0.0:8000
