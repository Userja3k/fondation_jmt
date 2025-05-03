#!/bin/bash
# This script runs on every deploy on Render

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Deployment release script completed."
