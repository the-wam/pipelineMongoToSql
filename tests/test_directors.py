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
    db = DirectorsSql(**config)
    
    directors = [("toto", "junior"), ("ta", "pator"), ("gfsfgdf", "pator"), ("", "final robert Carlos")]

    lenAllDirectors = len(db.selectDirectors())

    db.insertDirector(directors[0])
    db.insertDirectors(directors[1:-1])
    db.insertDirectorFullName(directors[-1][1])

    allDirectors = db.selectDirectors()
    assert len(allDirectors) == lenAllDirectors + len(directors)

    selectByName = db.selectDirectorByName(directors[0][0], directors[0][1])
    assert selectByName[1:-1] == directors[0]

    selectByID = db.selectDirectorByID(selectByName[0] + 1)
    assert selectByID[1:-1] == directors[1]

    db.updateDirector("final robert Carlos", "final", "robert Carlos")
    
    for director in directors[:-1]:
        actorId = db.selectDirectorByName(director[0], director[1])[0]
        db.deleteDirectorById(actorId)

    db.deleteDirectorById(selectByName[0] + 3)

    allDirectors = db.selectDirectors()
    assert len(allDirectors) == lenAllDirectors