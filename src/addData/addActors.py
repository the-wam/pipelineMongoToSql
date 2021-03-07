import logging as lg

from src.addData import AddMoviesFonctions
from src.database import ActorsSql
from src import openJson 
config = openJson("config/config.json")

class AddActors(AddMoviesFonctions):
    
    def __init__(self, movieDict, movieId):
        super().__init__(movieDict)
        self.movieId = movieId

    def runAddActors(self):

        # Connection database
        actorsDb = ActorsSql(**config)

        # returns the list of keys of my dictionary
        #listMovieKeys = movieDict.keys()

        # returns the list of actors
        actors = self.attributeValue('cast')

        
        # add relationships between film and actors
        if actors:
            for actor in actors:
                actorfullname = actor.split()
                if len(actorfullname) == 2:
                    actorId = actorsDb.selectActorByName(actorfullname[0], actorfullname[1])
                    if actorId:
                        selectCasting = actorsDb.selectCastingByActorIdMovieId(actorId[0], self.movieId)
                        if not selectCasting:
                            castingId = actorsDb.insertCasting(actorId[0], self.movieId)
                    else:
                        actorId = actorsDb.insertActor(actorfullname)
                        castingId = actorsDb.insertCasting(actorId, self.movieId)
                else:
                    actorId = actorsDb.selectActorByName(fullname=actor)
                    if actorId:
                        selectCasting = actorsDb.selectCastingByActorIdMovieId(actorId[0], self.movieId)
                        if not selectCasting:                   
                            castingId = actorsDb.insertCasting(actorId[0], self.movieId)
                    else:
                        actorId = actorsDb.insertActorFullName(actor)
                        castingId = actorsDb.insertCasting(actorId, self.movieId)
        else:
            castingId = None
        
        return castingId