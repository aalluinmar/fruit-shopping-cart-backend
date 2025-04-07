# Fruit Shopping Cart Backend

This is the backend for the Fruit Shopping Cart API built with Flask, SQLAlchemy, PostgreSQL, and Docker.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fruit-shopping-cart-backend.git
cd fruit-shopping-cart-backend
```

### 2. Create virtual environment

Run the below command to create virtual environment

```bash
python3 -m venv env
```

### 3. Active virtual environment

Activate virtual environment

```bash
source env/bin/activate
```

### 4. Install dependencies

Install python packages

```bash
pip3 install -r requirements/dev.txt
```

### 5. Run the application using Docker

Run the following command to build and start the Docker containers

```bash
docker-compose up --build
```

### 6. Database Migration

The migrations are automated using the entrypoint.sh script that runs every time the Flask app container starts. The script performs the following:
1. Runs flask db upgrade to apply any pending migrations.
2. If the migrations folder doesn't exist, it initializes it with flask db init.
3. Starts the Flask app with python3 run.py.
