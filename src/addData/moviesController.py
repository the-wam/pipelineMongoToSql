import logging as lg

from src.addData import AddMovie
from src.addData import AddGenres
from src.addData import AddActors
from src.addData import AddDirectors

class moviesController():
        
    def run(self, movies):

        for index, movie in enumerate(movies):

            lg.info(index, movie["title"])
            
            # add general informaion of movie
            movieToAdd = AddMovie(movie)
            movieId = movieToAdd.runAddMovie()
            
            # add genres
            genresToAdd = AddGenres(movie, movieId)
            genresToAdd.runAddGenres()

            # add Actors
            actrorsToAdd = AddActors(movie, movieId)
            actrorsToAdd.runAddActors()

            # add Directors
            directorsToAdd = AddDirectors(movie, movieId)
            directorsToAdd.runAddDirectors()


