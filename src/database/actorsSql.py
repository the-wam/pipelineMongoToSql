import mysql.connector
from mysql.connector import connect
from mysql.connector import IntegrityError
from mysql.connector import errorcode

from src import openJson
from src.database import ConnectionSql
import logging as lg
lg.basicConfig(level=lg.DEBUG)

class ActorsSql(ConnectionSql):

    def insertActors(self, listActors):
        """

        """

        cnx, cursor = self.connection()

        sql = "INSERT INTO Actors (firstname_a, lastname_a) VALUES (%s, %s)"
        val = listActors
        
        cursor.executemany(sql, val)
        
        cnx.commit()
                
        lg.info(f"{cursor.rowcount} record inserted.")
        self.close(cnx)

    def insertActorFullName(self, fullName): 
        """
        Pour les actrices/acteurs qui n'ont pas un nom complet 
        du type ("prénom" "nom"), ils sont ajouté à fullname 
        pour être traiter manuelement  
        """

        cnx, cursor = self.connection()

        sql = "INSERT INTO Actors (fullname_a) VALUES (%s)"
        val = fullName
        
        cursor.executemany(sql, val)
        
        cnx.commit()
                
        lg.info(f"{cursor.rowcount} record inserted.")
        self.close(cnx)

    def insertActor(self, actor):
        """

        """

        cnx, cursor = self.connection()

        sql = "INSERT INTO Actors (firstname_a, lastname_a) VALUES (%s, %s)"
        val = actor

        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record inserted.")
        self.close(cnx)    

    def selectActors(self): 

        cnx, cursor = self.connection()

        sql = "SELECT * FROM actors"

        cursor.execute(sql)

        listActors = cursor.fetchall()

        self.close(cnx)

        return listActors  
   
    def selectActorByID(self,actorsId):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM actors WHERE id_a = %s"
        val = [actorsId]
    
        cursor.execute(sql, val)

        actor = cursor.fetchone()

        self.close(cnx)
        
        return actor

    def selectActorByName(self,firstname = None, lastname =None):

        if not firstname and not lastname:
            return None
        elif firstname and not lastname:
            sql = "SELECT * FROM actors WHERE firstname_a = %s"
            val = [firstname]
        elif lastname and not firstname:
            sql = "SELECT * FROM actors WHERE lastname_a = %s"
            val = [lastname]
        else:
            sql = "SELECT * FROM actors WHERE firstname_a = %s and lastname_a = %s"
            val = [firstname, lastname]
        
        cnx, cursor = self.connection()

        cursor.execute(sql, val)

        listActors = cursor.fetchone()

        self.close(cnx)
        
        return listActors

    def selectActorsNull(self): 

        cnx, cursor = self.connection()

        sql = "SELECT * FROM actors WHERE firstname_a IS NULL"

        cursor.execute(sql)

        listActors = cursor.fetchall()

        self.close(cnx)

        return listActors

    def updateActor(self, oldName, newFirstname, newLastname):

        sql = "UPDATE actors set firstname_a = %s, lastname_a = %s WHERE lastname_a = %s"
        val = (newFirstname, newLastname, oldName)
        
        cnx, cursor = self.connection()
        cursor.execute(sql, val)
        
        cnx.commit()
        self.close(cnx)
        
        lg.info(f"{cursor.rowcount} updated")

    def deleteActorById(self, actorId):

        sql = "DELETE FROM actors WHERE id_a = %s"
        val = [actorId]

        cnx, cursor = self.connection()
        cursor.execute(sql, val)
        
        cnx.commit()
        self.close(cnx)
        
        lg.info(f"{cursor.rowcount} deleted") 