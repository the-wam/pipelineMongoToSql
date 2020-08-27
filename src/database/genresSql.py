import mysql.connector
from mysql.connector import connect
from mysql.connector import IntegrityError
from mysql.connector import errorcode

from src import openJson
from src.database import ConnectionSql
import logging as lg
lg.basicConfig(level=lg.DEBUG)

class GenresSql(ConnectionSql):

    def insertGenres(self, genres):
        
        cnx, cursor = self.connection()

        sql = "INSERT INTO Genres (name_g) VALUES (%s)"
        val = genres
        
        cursor.executemany(sql, val)
        
        cnx.commit()
        lg.info(f"{cursor.rowcount} record inserted.")

        self.close(cnx)

    def insertGenre(self, genre):

        cnx, cursor = self.connection()

        sql = "INSERT INTO Genres (name_g) VALUES (%s)"
        val = [genre]
        
        cursor.execute(sql, val)
        
        cnx.commit()
        lg.info(f"{cursor.rowcount} record inserted.")

        self.close(cnx)
    
    def selectGenres(self):

        cnx, cursor = self.connection()

        cursor.execute("SELECT * From Genres")

        listeGenres = cursor.fetchall()

        self.close(cnx)
        
        return listeGenres

    def selectGenreByName(self, name):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM Genres WHERE name_g = %s"
        val = [name]
        
        cursor.execute(sql, val)

        genreIdName = cursor.fetchone()

        self.close(cnx)
        
        return genreIdName

    def selectGenreById(self, id_g):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM Genres WHERE id_g = %s"
        val = [id_g]
        
        cursor.execute(sql, val)

        genreIdName = cursor.fetchone()

        self.close(cnx)
        
        return genreIdName

    def deleteGenreByName(self, name):
        
        cnx, cursor = self.connection()

        sql = "DELETE FROM genres WHERE name_g = %s"
        
        val = [name]

        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record deleted.")

        self.close(cnx)

    def deleteGenreByID(self, id_g):
        
        cnx, cursor = self.connection()

        sql = "DELETE FROM genres WHERE id_g = %s"
        val = [id_g]

        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record deleted.")

        self.close(cnx)
