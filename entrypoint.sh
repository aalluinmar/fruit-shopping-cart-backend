#!/bin/bash

# Set the Python path to include /app
export PYTHONPATH=$PYTHONPATH:/app

# Run migrations before starting the app
echo "Running database migrations..."
flask db upgrade

# If migrations folder does not exist, initialize it
if [ ! -d "migrations" ]; then
  echo "Initializing migrations..."
  flask db init
fi

# Start the Flask app
exec "$@"
