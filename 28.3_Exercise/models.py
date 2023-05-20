"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

stock_image="https://tinyurl.com/demo-cupcake"

def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()


class Cupcake(db.Model):
    """Cupcake Model"""

    __tablename__="cupcakes"

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor=db.Column(db.Text, nullable=False)
    size = db.Column(db.Text, nullable=False)
    rating=db.Column(db.Float, nullable=False)
    image=db.Column(db.Text, nullable=False, default=stock_image)

    """Serialize a cupcake instance so we can jsonify"""
    def serialize_cupcake(self):
        return {
            "flavor": self.flavor,
            "size": self.size,
            "rating": self.rating,
            "image": self.image

        }