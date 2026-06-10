from dao.directors import DirectorDAO
from dao.genres import GenreDAO
from dao.movies import MovieDAO
from services.directors import DirectorService
from services.genres import GenreService
from services.movies import MovieServices
from setup_db import db


movie_dao = MovieDAO(db.session)
movie_service = MovieServices(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)