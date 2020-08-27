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
    db = ActorsSql(config["host"], config["user"], config["password"], config["database"], config["port"])
    
    actors = [("toto", "junior"), ("ta", "pator"), ("", "final robert Carlos")]

    db.insertActor(actors[0])
    db.insertActors(actors[1:])

    allActors = db.selectActors()
    assert len(allActors) == numberOfActors + 3

    selectByName = db.selectActorByName(actors[0][0], actors[0][1])
    assert selectByName[1:] == actors[0]

    selectByID = db.selectActorByID(selectByName[0] + 1)
    assert selectByID[1:] == actors[1]

    db.updateActor("final robert Carlos", "final", "robert Carlos")
    
    for x in actors[:-1]:
        actorId = db.selectActorByName(x[0], x[1])[0]
        db.deleteActorById(actorId)

    db.deleteActorById(selectByName[0] + 2)

    allActors = db.selectActors()
    assert len(allActors) == numberOfActors