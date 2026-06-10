from flask import Flask
from flask_restx import Api

from config import Config
from dao.model.directors import Director
from dao.model.genres import Genre
from dao.model.movies import Movie
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.app_context().push()
    return app


def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)



def create_data():
    
    with app.app_context():


        g1 = Genre(name="Комедия")
        g2 = Genre(name="Фантастика")
            
        
        d1 = Director(name="Кристофер Нолан")
        d2 = Director(name="Тайка Вайтити")

        db.session.add_all([g1, g2, d1, d2])
        db.session.flush()
        
        m1 = Movie(
            title="Интерстеллар", 
            description="Путешествие сквозь пространство и время.", 
            trailer="https://youtu.be...", 
            year=2014, 
            rating=8.6,
            genre_id=g2.id,      
            director_id=d1.id    
        )

        m2 = Movie(
            title="Реальные упыри", 
            description="Жизнь четырех вампиров в современном мире.", 
            trailer="https://youtu.be...", 
            year=2014, 
            rating=7.4,
            genre_id=g1.id,     
            director_id=d2.id     
        )

        db.session.add_all([m1, m2])
        db.session.commit()


if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    register_extensions(app)
    create_data()
    app.run()


