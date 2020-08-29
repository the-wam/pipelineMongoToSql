import mysql.connector
from mysql.connector import connect
from mysql.connector import IntegrityError
from mysql.connector import errorcode

from src.database import ConnectionSql
import logging as lg
lg.basicConfig(level=lg.DEBUG)
#from src import openJson
#import logging as lg

# add config file


class MoviesSql(ConnectionSql):

    def insertMovie(self, title_m, year_m, imdb_rating_m, imdb_vote_m, poster_m, full_plot_m, tomates_viewer_m, tomates_critic_m, runtime_m):

        sql = """INSERT INTO movies (title_m, year_m,imdb_rating_m,imdb_vote_m,poster_m,full_plot_m,tomates_viewer_m,tomates_critic_m,runtime_m)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        val = (title_m, 
            year_m, 
            imdb_rating_m, 
            imdb_vote_m, 
            poster_m,
            full_plot_m, 
            tomates_viewer_m, 
            tomates_critic_m,
            runtime_m)  
        
        cnx, cursor = self.connection()
        cursor.execute(sql, val)

        cnx.commit()
                
        lg.info(f"{cursor.rowcount} record inserted.")
        self.close(cnx)


    def allMovies(self):

        sql =  "SELECT id_m, title_m FROM movies"

        cnx, cursor = self.connection()

        cursor.execute(sql)

        moviesList = cursor.fetchall()

        self.close(cnx)

        return moviesList


    def selectMoviesByName(self, movieTitle):

        sql = """ SELECT id_m, title_m FROM Movies WHERE title_m = %s"""

        val = [movieTitle]

        cnx, cursor = self.connection()

        cursor.execute(sql, val)

        moviesList = cursor.fetchall()

        self.close(cnx)

        return moviesList

    def selectMovieById(self, movieId):

        sql = """ SELECT id_m, title_m FROM Movies WHERE id_m = %s"""

        val = [movieId]

        cnx, cursor = self.connection()

        cursor.execute(sql, val)

        movie = cursor.fetchone()

        self.close(cnx)

        return movie
        

    def deleteMovieById(self, movieId):

        sql = "DELETE FROM Movies WHERE id_m = %s"

        val = [movieId]

        cnx, cursor = self.connection()

        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record deleted.")

        self.close(cnx)

