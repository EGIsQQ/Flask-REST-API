from setup_db import db
from marshmallow import Schema, fields

class Director(db.Model):
    __tablename__ = 'directors'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150), nullable=False)
    movies = db.relationship('Movie', backref='director', lazy=True)

class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()