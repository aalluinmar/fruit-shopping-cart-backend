from app import db


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fruit_id = db.Column(db.Integer, db.ForeignKey('fruit.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
