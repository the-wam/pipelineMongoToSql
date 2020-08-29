import pytest

from src.database import GenresSql
from src import openJson

# Comnnection Database
config = openJson("config/config.json")

# Database values :
dbValues = openJson("config/dbValues.json")
numberOfGenres = dbValues["numberOfGenres"]


@pytest.mark.genres
def test_genreByName():
    db = GenresSql(config["host"], config["user"], config["password"], config["database"], config["port"])

    toto1 = "toto1"

    # test function insert one genre
    db.insertGenre(toto1)

    # test function select by name
    res = db.selectGenreByName(toto1)

    # test function delete by name
    db.deleteGenreByName("toto1")

    # test select, FORMAT : [(1, 'Action'), (3, 'Adventure'), (4, 'Drama'), (5, 'Sci-Fi'), (6, 'News'), (7, 'Romance'), ...]
    allGenre = db.selectGenres()

    assert res[1] == toto1
    assert len(allGenre) == numberOfGenres
@pytest.mark.genres
def test_genresById():
    db = GenresSql(config["host"], config["user"], config["password"], config["database"], config["port"])

    toto2 = [("toto2", ), ("toto3",)]

    db.insertGenres(toto2)

    # select FORMAT : [(1, 'Action'), (3, 'Adventure'), (4, 'Drama'), (5, 'Sci-Fi'), (6, 'News'), (7, 'Romance'), ...]
    listGenres  = db.selectGenres()

    # assert if add work 
    assert len(listGenres) == numberOfGenres + 2

    # test select by Id
    for genre in listGenres:
        if genre[1] == toto2[0][0]:
            res1 = db.selectGenreById(genre[0])
            
        if genre[1] == toto2[1][0]:
            res2 = db.selectGenreById(genre[0])

    # test delete by Id
    db.deleteGenreByID(res1[0])
    db.deleteGenreByID(res2[0])

    # assert return to initial situation
    listGenres  = db.selectGenres()

    assert len(listGenres) == numberOfGenres