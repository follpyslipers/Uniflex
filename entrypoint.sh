#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Print environment variables for debugging
echo "Environment variables:"
printenv

# Apply database migrations
echo "Making and applying database migrations..."
python manage.py makemigrations
python manage.py migrate

# Add a delay to ensure everything is set up
sleep 10

# Start the Django development server
echo "Starting Django development server on port ${PORT:-8000}..."
exec python manage.py runserver 0.0.0.0:${PORT:-8000}
