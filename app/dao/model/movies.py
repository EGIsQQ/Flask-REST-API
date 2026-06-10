from setup_db import db
from marshmallow import Schema, fields

class Movie(db.Model):
    __tablename__ = 'movies'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    trailer = db.Column(db.String(500), nullable=True)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, default=0.0)
    
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'), nullable=False)


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()