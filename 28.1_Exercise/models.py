from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

class Pet(db.Model):
    """create Pet model"""
    __tablename__= "pets"

    id=db.Column(db.Integer, autoincrement=True, primary_key=True)
    name=db.Column(db.Text, nullable=False)
    species=db.Column(db.Text, nullable=False)
    photo_url=db.Column(db.Text)
    age=db.Column(db.Integer)
    notes=db.Column(db.Text)
    available=db.Column(db.Boolean, default=True, nullable=False)