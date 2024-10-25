#!/bin/bash

# Exit the script on any error
set -o errexit

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Collect static files (for production use)
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py migrate
