"""Models for Adopt."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet SQL Model"""

    def __repr__(self):
        return f"Id: {self.id} Name:{self.name} Species: {self.species} Avail: {self.available}"

    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), nullable=False)
    species = db.Column(db.String(25), nullable=False)
    photo_url = db.Column(db.Text, nullable=True, default="https://image.shutterstock.com/image-vector/vector-black-silhouette-dog-isolated-260nw-563030956.jpg")
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.String(160), nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)
