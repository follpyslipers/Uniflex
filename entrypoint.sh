#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Apply database migrations
echo "Making and applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Start the Django development server
echo "Starting Django development server..."
exec python manage.py runserver 0.0.0.0:${PORT:-8000}
