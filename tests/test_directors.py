import pytest

from src.database import DirectorsSql
from src import openJson

# Comnnection Database
config = openJson("config/config.json")

# Database values :
dbValues = openJson("config/dbValues.json")
numberOfDirectors = dbValues["numberOfDirectors"]

@pytest.mark.directors
def test_directors():
    db = DirectorsSql(config["host"], config["user"], config["password"], config["database"], config["port"])
    
    directors = [("toto", "junior"), ("ta", "pator"), ("", "final robert Carlos")]

    db.insertDirector(directors[0])
    db.insertDirectors(directors[1:])

    allDirectors = db.selectDirectors()
    assert len(allDirectors) == numberOfDirectors + 3

    selectByName = db.selectDirectorByName(directors[0][0], directors[0][1])
    assert selectByName[1:] == directors[0]

    selectByID = db.selectDirectorByID(selectByName[0] + 1)
    assert selectByID[1:] == directors[1]

    db.updateDirector("final robert Carlos", "final", "robert Carlos")
    
    for x in directors[:-1]:
        actorId = db.selectDirectorByName(x[0], x[1])[0]
        db.deleteDirectorById(actorId)

    db.deleteDirectorById(selectByName[0] + 2)

    allDirectors = db.selectDirectors()
    assert len(allDirectors) == numberOfDirectors