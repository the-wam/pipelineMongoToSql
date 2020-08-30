import pytest

from src.database import MoviesSql
from src import openJson

import logging as lg
lg.basicConfig(level=lg.DEBUG)

# Comnnection Database
config = openJson("config/config.json")

# Database values :
dbValues = openJson("config/dbValues.json")
numberOfMovies = dbValues["numberOfMovies"]

@pytest.mark.movies
def test_movies():

    movie = {'_id': {'$oid': '573a1390f29313caabcd4135'},
            'plot': 'Three men hammer on an anvil and pass a bottle of beer around.',
            'genres': ['Short'],
            'poster': 'url_link',
            'cast': ['Charles Kayser', 'John Ott'],
            'title': 'titre1',
            'fullplot': 'A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.',
            'countries': ['USA'],
            'directors': ['William Dickson'],
            'rated': 'UNRATED',
            'year': 1993,
            'imdb': {'rating': 6.2, 'votes': 1189},
            'type': 'movie',
            'tomatoes': {'viewer': {'rating': 3, 'numReviews': 184, 'meter': 32}, 'critic': {'rating': 2, 'numReviews': 12, 'meter': 56}},
            'runtime': 137}

    db = MoviesSql(**config)
        
    movieId = db.insertMovie(movie["title"],
        movie["year"],
        movie["imdb"]["rating"],
        movie["imdb"]["votes"],
        movie["poster"],
        movie["fullplot"],
        movie["tomatoes"]["viewer"]["rating"],
        movie["tomatoes"]["critic"]["rating"],
        movie["runtime"])

    listMovies = db.allMovies()
    assert len(listMovies) == numberOfMovies + 1

    movieInserted = db.selectMoviesByName(movie["title"])
    assert movieInserted[0][0] == movieId 
    assert movieInserted[0][1] == movie["title"]
    assert movieInserted[0][2] == movie["year"]

    movieById = db.selectMovieById(movieId)
    assert movieById[1] == movie["title"]
    assert movieById[2] == movie["year"]

    db.deleteMovieById(movieId)

    listMovies = db.allMovies()
    assert len(listMovies) == numberOfMovies