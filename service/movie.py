from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movies(self):
        result = self.db.query(MovieModel).all()
        return result

    def get_movie_by_id(self, id: int):
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movie_by_title(self, title: str):
        result = self.db.query(MovieModel).filter(MovieModel.title == title).first()
        return result
        

    def create_movie(self, movie:MovieModel):
        new_movie = MovieModel(
        title=movie.title,
        overview = movie.overview,
        year = movie.year,
        time = movie.time,
        date_release = movie.date_release,
        release_contry = movie.release_contry
        )
        self.db.add(new_movie)
        self.db.commit()
        return 

    def update_movie(self,id:int, data:MovieModel):
        movie = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.time = data.time
        movie.date_release = data.date_release
        movie.release_contry = data.release_contry
        self.db.commit()
        return

    def delete_movie(self, id: int):
        movie = self.get_movie_by_id(id)
        if not movie:
            return None
        self.db.delete(movie)
        self.db.commit()
        return movie

    def get_movie_by_id(self, id: int):
        return self.db.query(MovieModel).filter(MovieModel.id == id).first()