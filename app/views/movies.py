from flask_restx import Resource, Namespace
from dao.model.movies import MovieSchema
from container import movie_service
from flask import request

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director_id = request.args.get('director_id', type=int)
        genre_id = request.args.get('genre_id', type=int)
        year = request.args.get('year', type=int)
        movies = movie_service.get_movies(director_id, genre_id, year)
        return movies_schema.dump(movies), 200
        

    def post(self):
        req = request.json
        movie_service.create_movie(req)
        return "", 201

@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req = request.json
        req['id'] = mid

        movie_service.update(req)
        return "", 204
    
    def delete(self, mid): 
        movie_service.delete(mid)
        return '', 204


