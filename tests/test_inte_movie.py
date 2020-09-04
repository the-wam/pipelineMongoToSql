import pytest


from src import openJson
from src.database import GenresSql, MoviesSql, DirectorsSql, ActorsSql
from src.addData import attributeValue, addMovieControler, movieGenres, moviesActors, moviesDirectors

import logging as lg
lg.basicConfig(level=lg.DEBUG)

# Comnnection Database
config = openJson("config/config.json")


@pytest.mark.addMovie
def test_addMovie():

    # Data for Test
    movie = {'_id': {'$oid': '573a1390f29313caabcd4135'},
            'plot': 'Three men hammer on an anvil and pass a bottle of beer around.',
            'genres': ['Shxvsxort'],
            'poster': 'url_link',
            'cast': ['Charlesaa Kayseraa'],
            'title': 'titre',
            'fullplot': 'A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.',
            'countries': ['USA'],
            'directors': ['William efrsfs Dickson'],
            'rated': 'UNRATED',
            'year': 1992,
            'imdb': {'rating': 6.2, 'votes': 1189},
            'type': 'movie',
            'tomatoes': {'viewer': {'rating': 3, 'numReviews': 184, 'meter': 32}},
            'runtime': 137}

    # Add general parameters of movie
    movieId = addMovieControler(movie)


    # Connection database and assert if we find this movie
    db = MoviesSql(**config)

    
    movieSqlTitre = db.selectMoviesByName(movie["title"])
    movieSqlId = db.selectMovieById(movieId)

    assert movieSqlTitre[0] == movieSqlId
    assert movieSqlId[0] == movieId # 
    assert movieSqlId[1] == movie["title"] # check title
    assert movieSqlId[2] == movie["year"] # check year
    assert movieSqlId[3] == movie["runtime"] # check runtime
    assert movieSqlId[4] == None # check None tomates_critic

    
    # Add types of this movie
    typesId = movieGenres(movie, movieId)
    dbGenres = GenresSql(**config)
    genreId = dbGenres.selectGenreByName(movie['genres'][0])[0]
    assert dbGenres.selectTypeMovieById(typesId) == (typesId, movieId, genreId)

    # Add Actors of this movie
    castingId = moviesActors(movie, movieId)
    dbActors = ActorsSql(**config)
    actorId = dbActors.selectActorByName('Charlesaa', 'Kayseraa')[0]
    assert dbActors.selectCastingById(castingId) == (castingId, actorId, movieId)

    # Add Actors of this movie
    directingId = moviesDirectors(movie, movieId)
    dbDirectors = DirectorsSql(**config)
    directorId = dbDirectors.selectDirectorByName(fullname=movie["directors"][0])[0] 
    assert dbDirectors.selectDirectingById(directingId) == (directingId, directorId, movieId)



    # Delete data's test
    
    dbGenres.deleteTypeMovieById(typesId)
    dbGenres.deleteGenreByName(movie["genres"][0])

    dbActors.deleteCastingById(castingId)
    dbActors.deleteActorById(actorId)

    dbDirectors.deleteDirectingById(directingId)
    dbDirectors.deleteDirectorById(directorId)

    db.deleteMovieById(movieId)







