import logging as lg

from src.addData import AddMoviesFonctions
from src.database import GenresSql
from src import openJson
config = openJson("config/config.json")


class AddGenres(AddMoviesFonctions):

    def __init__(self, movieDict, movieId):
        super().__init__(movieDict)
        self.movieId = movieId

    def runAddGenres(self):
        
        # Connection database
        genresDB = GenresSql(**config)

        # returns the list of keys of my dictionary
        # listMovieKeys = movieDict.keys()

        # returns the list of genres
        genres = self.attributeValue("genres")

        # add relationships between film and genres
        typeMoviesId = None
        if genres:
            for genre in genres:
                genreId = genresDB.selectGenreByName(genre)
                if genreId:
                    selectType = genresDB.selectTypeMovieByGenreIdMovieId(genreId[0], self.movieId)
                    if not selectType:
                        typeMoviesId = genresDB.insertTypeMovie(genreId[0], self.movieId)
                else:
                    genreId = genresDB.insertGenre(genre)
                    typeMoviesId = genresDB.insertTypeMovie(genreId, self.movieId)

        return typeMoviesId