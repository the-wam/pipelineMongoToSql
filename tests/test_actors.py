import pytest

from src.database import ActorsSql
from src import openJson

# Comnnection Database
config = openJson("config/config.json")

# Database values :
dbValues = openJson("config/dbValues.json")
numberOfActors = dbValues["numberOfActors"]

@pytest.mark.actors
def test_actors():
    db = ActorsSql(**config)
    
    actors = [("toto", "junior"), ("ta", "pator"), ("gfsfgdf", "pator"), ("", "final robert Carlos")]

    lenAllActors = len(db.selectActors())

    db.insertActor(actors[0])
    db.insertActors(actors[1:-1])
    db.insertActorFullName(actors[-1][1])

    lenAllActorsInsert = len(db.selectActors())

    assert lenAllActorsInsert == lenAllActors + len(actors)

    selectByName = db.selectActorByName(actors[0][0], actors[0][1])
    assert selectByName[1:-1] == actors[0]

    selectByID = db.selectActorByID(selectByName[0] + 1)
    assert selectByID[1:-1] == actors[1]

    db.updateActor("final robert Carlos", "final", "robert Carlos")
    
    for actor in actors[:-1]:
        actorId = db.selectActorByName(actor[0], actor[1])[0]
        db.deleteActorById(actorId)

    db.deleteActorById(selectByName[0] + 3)

    allActors = db.selectActors()
    assert len(allActors) == lenAllActors
