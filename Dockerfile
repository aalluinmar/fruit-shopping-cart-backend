# Dockerfile

# Use Python 3.12 slim base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev

# Install Python dependencies
COPY requirements/dev.txt .
RUN pip3 install -r dev.txt

# Copy the rest of the application code
COPY . .

# Expose the port dynamically based on .env or docker-compose
EXPOSE ${FLASK_RUN_PORT}

# Add entrypoint script to automatically handle migrations
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Use the entrypoint script
ENTRYPOINT ["/entrypoint.sh"]

# Start the Flask app (this will be run after migration)
CMD ["python3", "app/run.py"]
