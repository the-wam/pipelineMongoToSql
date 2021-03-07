import logging as lg

from src.addData import AddMoviesFonctions
from src.database import DirectorsSql
from src import openJson
config = openJson("config/config.json")

class AddDirectors(AddMoviesFonctions):

    def __init__(self, movieDict, movieId):
        super().__init__(movieDict)
        self.movieId = movieId

    def runAddDirectors(self):

        # Connection database
        directorsDb = DirectorsSql(**config)

        # returns the list of keys of my dictionary
        # listMovieKeys = movieDict.keys()

        # returns the list of directors
        directors = self.attributeValue('directors')

        # add relationships between film and directors
        
        if directors:
            for director in directors:
                directorfullname = director.split()
                if len(directorfullname) == 2:
                    directorId = directorsDb.selectDirectorByName(directorfullname[0], directorfullname[1])
                    if directorId:
                        directingId = directorsDb.selectDirectingByDirectorIdMovieId(directorId[0], self.movieId)
                        if not directingId:
                            directingId = directorsDb.insertDirectingBy(directorId[0], self.movieId)
                    else:
                        directorId = directorsDb.insertDirector(directorfullname)
                        directingId = directorsDb.insertDirectingBy(directorId, self.movieId)
                else:
                    directorId = directorsDb.selectDirectorByName(fullname=director)
                    if directorId:
                        directingId = directorsDb.selectDirectingByDirectorIdMovieId(directorId[0], self.movieId)
                        if not directingId:
                            directingId = directorsDb.insertDirectingBy(directorId[0], self.movieId)
                    else:
                        directorId = directorsDb.insertDirectorFullName(director)
                        directingId = directorsDb.insertDirectingBy(directorId, self.movieId)
        else:
            directingId = None
        
        return directingId