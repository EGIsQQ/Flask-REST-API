
class MovieServices: 
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)
    
    def get_all(self): 
        return self.dao.get_all()
    
    def get_movies(self, director_id=None, genre_id=None, year=None): 
        movies = self.dao.get_movies(director_id, genre_id, year)
        return movies
    
    def create_movie(self, data): 
        return self.dao.create(data)
    
    def update(self, data): 
        mid = data.get('id')
        movie = self.get_one(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year') 
        movie.rating = data.get('rating') 

        self.dao.update(movie)  

    def delete(self, mid): 
        self.dao.delete(mid) 