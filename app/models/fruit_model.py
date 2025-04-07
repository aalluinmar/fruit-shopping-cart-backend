from app.db import db


class Fruit(db.Model):
    __tablename__ = "fruits"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Fruit {self.name}>"
