import pytest

from src.database import GenresSql
from src import openJson

# Comnnection Database
config = openJson("config/config.json")



@pytest.mark.genres
def test_genreByName():
    db = GenresSql(**config)

    lenAllGenre = len(db.selectGenres())

    toto1 = "toto1"

    # test function insert one genre
    db.insertGenre(toto1)

    allGenre = db.selectGenres()
    assert len(allGenre) == lenAllGenre + 1
    # test function select by name
    res = db.selectGenreByName(toto1)

    # test function delete by name
    db.deleteGenreByName("toto1")

    # test select, FORMAT : [(1, 'Action'), (3, 'Adventure'), (4, 'Drama'), (5, 'Sci-Fi'), (6, 'News'), (7, 'Romance'), ...]
    allGenre = db.selectGenres()

    assert res[1] == toto1
    assert len(allGenre) == lenAllGenre

    
@pytest.mark.genres
def test_genresById():
    db = GenresSql(**config)

    toto2 = [("toto2", ), ("toto3",)]

    lenAllGenre = len(db.selectGenres())
    db.insertGenres(toto2)

    # select FORMAT : [(1, 'Action'), (3, 'Adventure'), (4, 'Drama'), (5, 'Sci-Fi'), (6, 'News'), (7, 'Romance'), ...]
    listGenres  = db.selectGenres()

    # assert if add work 
    assert len(listGenres) == lenAllGenre + 2

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

    assert len(listGenres) == lenAllGenre


@pytest.mark.lastInsertId
def test_lastInsertId():
    db = GenresSql(**config)

    genre = ["insert", "tut"]

    db.insertGenre(genre[0])

    test2 = db.insertGenre(genre[1])

    assert db.selectGenreByName(genre[0])[1] == genre[0]
    assert db.selectGenreById(test2)[1] == genre[1]

    db.deleteGenreByName(genre[0])
    db.deleteGenreByName(genre[1])
