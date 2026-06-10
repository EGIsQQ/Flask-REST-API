from marshmallow import Schema, fields
from setup_db import db

class Genre(db.Model):
    __tablename__ = 'genres'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    
    movies = db.relationship('Movie', backref='genre', lazy=True)

class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

