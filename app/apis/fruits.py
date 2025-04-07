from flask import Blueprint, request, jsonify
from app.models.fruit_model import Fruit
from app.db import get_db_session

fruits_bp = Blueprint("fruits", __name__)

@fruits_bp.route("/", methods=["GET"])
def get_fruits():
    session = get_db_session()
    fruits = session.query(Fruit).all()
    return jsonify([{"id": fruit.id, "name": fruit.name, "price": fruit.price} for fruit in fruits]), 200

@fruits_bp.route("/", methods=["POST"])
def add_fruit():
    data = request.get_json()
    name = data.get("name")
    price = data.get("price")

    if not name or not price:
        return jsonify({"error": "Name and Price required"}), 400

    session = get_db_session()
    new_fruit = Fruit(name=name, price=price)
    session.add(new_fruit)
    session.commit()

    return jsonify({"message": "Fruit added successfully", "fruit_id": new_fruit.id}), 201
