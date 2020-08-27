import mysql.connector
from mysql.connector import connect
from mysql.connector import IntegrityError
from mysql.connector import errorcode

from src import openJson
from src.database import ConnectionSql
import logging as lg
lg.basicConfig(level=lg.DEBUG)

class DirectorsSql(ConnectionSql):

    def insertDirectors(self, listDirectors):
        """

        """

        cnx, cursor = self.connection()

        sql = "INSERT INTO Directors (firstname_d, lastname_d) VALUES (%s, %s)"
        val = listDirectors
        
        cursor.executemany(sql, val)
        
        cnx.commit()
                
        lg.info(f"{cursor.rowcount} record inserted.")
        self.close(cnx)

    def insertDirectorsFullName(self, fullName): 
        """
        Pour les réalisatrise/réalisateur qui n'ont pas un nom complet 
        du type ("prénom" "nom"), ils sont ajouté à fullname 
        pour être traiter manuelement  
        """

        cnx, cursor = self.connection()

        sql = "INSERT INTO Directors (fullname_d) VALUES (%s)"
        val = fullName
        
        cursor.executemany(sql, val)
        
        cnx.commit()
                
        lg.info(f"{cursor.rowcount} record inserted.")
        self.close(cnx)

    def insertDirector(self, director):
        """

        """

        cnx, cursor = self.connection()

        sql = "INSERT INTO Directors (firstname_d, lastname_d) VALUES (%s, %s)"
        val = director

        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record inserted.")
        self.close(cnx)

    def selectDirectors(self):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM Directors"

        cursor.execute(sql)

        listDirectors = cursor.fetchall()

        self.close(cnx)

        return listDirectors
   
    def selectDirectorByID(self,directorId):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM Directors WHERE id_d = %s"
        val = [directorId]
    
        cursor.execute(sql, val)

        director = cursor.fetchone()

        self.close(cnx)
        
        return director

    def selectDirectorByName(self,firstname = None, lastname =None):

        if not firstname and not lastname:
            return None
        elif firstname and not lastname:
            sql = "SELECT * FROM Directors WHERE firstname_d = %s"
            val = [firstname]
        elif lastname and not firstname:
            sql = "SELECT * FROM Directors WHERE lastname_d = %s"
            val = [lastname]
        else:
            sql = "SELECT * FROM Directors WHERE firstname_d = %s and lastname_d = %s"
            val = [firstname, lastname]
        
        cnx, cursor = self.connection()

        cursor.execute(sql, val)

        listDirectors = cursor.fetchone()

        self.close(cnx)
        
        return listDirectors

    def selectDirectorsNull(self): 

        cnx, cursor = self.connection()

        sql = "SELECT * FROM Directors WHERE firstname_d IS NULL"

        cursor.execute(sql)

        listDirectors = cursor.fetchall()

        self.close(cnx)

        return listDirectors

    def updateDirector(self, oldName, newFirstname, newLastname):

        sql = "UPDATE Directors set firstname_d = %s, lastname_d = %s WHERE lastname_d = %s"
        val = (newFirstname, newLastname, oldName)
        
        cnx, cursor = self.connection()
        cursor.execute(sql, val)
        
        cnx.commit()
        self.close(cnx)
        
        lg.info(f"{cursor.rowcount} updated")

    def deleteDirectorById(self, directorId):

        sql = "DELETE FROM Directors WHERE id_d = %s"
        val = [directorId]

        cnx, cursor = self.connection()
        cursor.execute(sql, val)
        
        cnx.commit()
        self.close(cnx)
        
        lg.info(f"{cursor.rowcount} deleted") 