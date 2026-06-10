from dao.model.movies import Movie


class MovieDAO: 
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)
    
    def get_all(self): 
        return self.session.query(Movie).all()
    
    def get_movies(self, director_id, genre_id, year):
        query = self.session.query(Movie).all()

        if director_id is not None: 
            query = self.session.query(Movie).filter(director_id == director_id).all()
        
        if genre_id is not None: 
            query = self.session.query(Movie).filter(genre_id == genre_id).all()

        if year is not None: 
            query = self.session.query(Movie).filter(year == year).all()

        return query 
    
    def create(self, data): 
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie
    
    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie        
    
    def delete(self, mid): 
        movie = self.get_one(mid)
        self.session.delete(movie)
        self.session.commit()

        

