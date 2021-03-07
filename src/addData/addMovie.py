import logging as lg

from src.addData import AddMoviesFonctions
from src.database import MoviesSql
from src import openJson
config = openJson("config/config.json")

class AddMovie(AddMoviesFonctions):

    def __init__(self, movieDict):
        super().__init__(movieDict)


    def getTitle(self):
        """
        Return the movie title 

        Return :
            title (str) = title of movie
        """
        if "title" in self.listMovieKeys:
            return self.movieDict["title"]
        else:
            lg.critical(f"This data has not title : {self.movieDict}")
            return ""
            

    def getYear(self):
        """
        Return the movie year 

        Return :
            year (int) : year of movie
        """

        return self.attributeValue("year")


    def getPoster(self):
        """
            Return the link of the poster's movie

            Return : 
                poster (str)
        """

        return self.attributeValue("poster")

    
    def getFullPlot(self):
        """
            Return the full plot's movie

            Return : 
                fullPlot (str) 
        """

        return self.attributeValue("fullplot")


    def getRuntime(self):   
        """
            Return the runtime's movie

            Return : 
                runtime (int) 
        """
        return self.attributeValue("runtime")


    def getImdb(self):
        """
            Return the imdb notes of movie

            Return : 
                imdbRating, imdbVote (int, int) 
        """

        if "imdb" in self.listMovieKeys:
            listMovieImdbKeys = self.movieDict["imdb"].keys()

            imdbRating = self.checkKeyValueInt("rating", listMovieImdbKeys, self.movieDict["imdb"])

            imdbVote = self.checkKeyValueInt("votes", listMovieImdbKeys, self.movieDict["imdb"])

            return imdbRating, imdbVote
        else:
            return 0, 0
    
    
    def getTomatoes(self):
        """
            Return the Tomatoes notes of movie

            Return : 
                tomatesViewer, tomatesCritic (int, int) 
        """
        if "tomatoes" in self.listMovieKeys:
            listMovieTomatoesKeys = self.movieDict["tomatoes"].keys()
            if "viewer" in listMovieTomatoesKeys:
                listMovieTomatoesViewerKeys = self.movieDict["tomatoes"]["viewer"]
                tomatesViewer = self.checkKeyValueInt("rating", listMovieTomatoesViewerKeys, self.movieDict["tomatoes"]["viewer"])
            else:
                tomatesViewer = 0
            
            if "critic" in listMovieTomatoesKeys:
                listMovieTomatoesCriticKeys = self.movieDict["tomatoes"]["critic"]
                tomatesCritic = self.checkKeyValueInt("rating", listMovieTomatoesCriticKeys, self.movieDict["tomatoes"]["critic"])
            else:
                tomatesCritic = 0
            
            return tomatesViewer, tomatesCritic

        else:
            return 0, 0

    def runAddMovie(self):
        """
            add general informaion of movie

            Return : 
                movieId (int)
        """

        title = self.getTitle()
        year = self.getYear()
        imdbRating, imdbVote = self.getImdb()
        poster = self.getPoster()
        fullPlot = self.getFullPlot()
        tomatesViewer, tomatesCritic = self.getTomatoes()
        runtime = self.getRuntime()

        movieDB = MoviesSql(**config)
        movieId = movieDB.selectMovieByNameYearRuntime(title, year, runtime)
        
        if not movieId:
            movieId = movieDB.insertMovie(title, year, imdbRating, imdbVote, poster, fullPlot, tomatesViewer, tomatesCritic, runtime)
            return movieId
        return movieId[0]
