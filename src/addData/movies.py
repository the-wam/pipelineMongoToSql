from mysql.connector import IntegrityError
import logging as lg
lg.basicConfig(level=lg.DEBUG)

from src.database import GenresSql, MoviesSql, DirectorsSql, ActorsSql
from src import openJson
config = openJson("config/config.json")

def attributeValue(keyName, listOfKeys, dataOneDict):

    if keyName in listOfKeys:
        return dataOneDict[keyName]
    else:
        lg.info(f"{str(dataOneDict['title'])} has not {keyName}")

        return None


def addMovieControler(dataOneDict):

    listMovieKeys = dataOneDict.keys()

    if "title" in listMovieKeys:
        title_m = dataOneDict["title"]
    else:
        lg.critical(f"This data has not title : {dataOneDict}")
        return False

    year_m = attributeValue("year", listMovieKeys, dataOneDict)

    poster_m = attributeValue("poster", listMovieKeys, dataOneDict)

    full_plot_m = attributeValue("fullplot", listMovieKeys, dataOneDict)

    runtime_m = attributeValue("runtime", listMovieKeys, dataOneDict)

    if "imdb" in listMovieKeys:
        listMovieImdbKeys = dataOneDict["imdb"].keys()

        imdb_rating_m = attributeValue("rating", listMovieImdbKeys, dataOneDict["imdb"])

        imdb_vote_m = attributeValue("votes", listMovieImdbKeys, dataOneDict["imdb"])
    else:
        imdb_rating_m, imdb_vote_m= None, None
    
    if "tomatoes" in listMovieKeys:
        listMovieTomatoesKeys = dataOneDict["tomatoes"].keys()
        if "viewer" in listMovieTomatoesKeys:
            listMovieTomatoesViewerKeys = dataOneDict["tomatoes"]["viewer"]
            tomates_viewer_m = attributeValue("rating", listMovieTomatoesViewerKeys, dataOneDict["tomatoes"]["viewer"])
        else:
            tomates_viewer_m = None
        
        if "critic" in listMovieTomatoesKeys:
            listMovieTomatoesCriticKeys = dataOneDict["tomatoes"]["critic"]
            tomates_critic_m = attributeValue("rating", listMovieTomatoesCriticKeys, dataOneDict["tomatoes"]["critic"])
        else:
            tomates_critic_m = None
        
    else:
        tomates_viewer_m, tomates_critic_m = None, None

    try:
        movieDB = MoviesSql(**config)
        movieId = movieDB.insertMovie(title_m, year_m, imdb_rating_m, imdb_vote_m, poster_m, full_plot_m, tomates_viewer_m, tomates_critic_m, runtime_m)
        
    except IntegrityError as e:
        lg.info(f"{str(title_m)} already exist")
        lg.info(e)
        movieId = None

    return movieId


def movieGenres(dataOneDict, movieId):
    
    # Connection database
    genresDB = GenresSql(**config)

    # returns the list of keys of my dictionary
    listMovieKeys = dataOneDict.keys()

    # returns the list of genres
    genres = attributeValue("genres", listMovieKeys, dataOneDict)

    # add relationships between film and genres
    if genres: 
        for genre in genres:
            genreId = genresDB.selectGenreByName(genre)
            if genreId:
                typeMoviesId = genresDB.insertTypeMovie(genreId[0], movieId)
            else:
                genreId = genresDB.insertGenre(genre)
                typeMoviesId = genresDB.insertTypeMovie(genreId, movieId)

    return typeMoviesId

def moviesActors(dataOneDict, movieId):

    # Connection database
    actorsDb = ActorsSql(**config)

    # returns the list of keys of my dictionary
    listMovieKeys = dataOneDict.keys()

    # returns the list of actors
    actors = attributeValue('cast', listMovieKeys, dataOneDict)
    # add relationships between film and actors
    if actors:
        for actor in actors:
            actorfullname = actor.split()
            if len(actorfullname) == 2:
                actorId = actorsDb.selectActorByName(actorfullname[0], actorfullname[1])
                if actorId:
                    castingId = actorsDb.insertCasting(actorId[0], movieId)
                else:
                    actorId = actorsDb.insertActor(actorfullname)
                    castingId = actorsDb.insertCasting(actorId, movieId)
            else:
                actorId = actorsDb.selectActorByName(fullname=actor)
                if actorId:
                    castingId = actorsDb.insertCasting(actorId[0], movieId)
                else:
                    actorId = actorsDb.insertActor(actor)
                    castingId = actorsDb.insertCasting(actorId, movieId)
    
    return castingId

def moviesDirectors(dataOneDict, movieId):

    # Connection database
    directorsDb = DirectorsSql(**config)

    # returns the list of keys of my dictionary
    listMovieKeys = dataOneDict.keys()

    # returns the list of directors
    directors = attributeValue('directors', listMovieKeys, dataOneDict)

    # add relationships between film and directors
    if directors:
        for director in directors:
            directorfullname = director.split()
            if len(directorfullname) == 2:
                directorId = directorsDb.selectDirectorByName(directorfullname[0], directorfullname[1])
                if directorId:
                    directingId = directorsDb.insertDirectingBy(directorId[0], movieId)
                else:
                    directorId = directorsDb.insertDirector(directorfullname)
                    directingId = directorsDb.insertDirectingBy(directorId, movieId)
            else:
                directorId = directorsDb.selectDirectorByName(fullname=director)
                if directorId:
                    directingId = directorsDb.insertDirectingBy(directorId[0], movieId)
                else:
                    directorId = directorsDb.insertDirector(director)
                    directingId = directorsDb.insertDirectingBy(directorId, movieId)
    
    return directingId


