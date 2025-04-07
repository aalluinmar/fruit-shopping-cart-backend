from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprints
    from app.apis import fruits, orders
    app.register_blueprint(fruits.fruits_bp, url_prefix="/api/fruits")
    app.register_blueprint(orders.orders_bp, url_prefix="/api/orders")

    return app
