import mysql.connector
from mysql.connector import connect
from mysql.connector import IntegrityError
from mysql.connector import errorcode

from src import openJson
from src.database import ConnectionSql
import logging as lg
#lg.basicConfig(level=lg.DEBUG)

class ActorsSql(ConnectionSql):

    ##########################################################################################################################################
    ##########################################################################################################################################
                                                                   # Actors
    ##########################################################################################################################################
    ##########################################################################################################################################

    def insertActors(self, listActors):
        """
        insert of this actors
        FORMAT [(firstname_a, lastname_a), (firstname_a, lastname_a)...]

        return Id of the last row add
        """

        sql = "INSERT INTO Actors (firstname_a, lastname_a) VALUES (%s, %s)"
        val = listActors
        
        cnx, cursor = self.connection()
        cursor.executemany(sql, val)
        
        cnx.commit()
                
        lg.info(f"{cursor.rowcount} record inserted.")

        lastActorId = cursor.lastrowid
        self.close(cnx)

        return lastActorId


    def insertActor(self, actor):
        """
        insert one Actor 

        FORMAT : (firstname_a, lastname_a)

        return id of actor inserted
        FORMAT : int
        """

        sql = "INSERT INTO Actors (firstname_a, lastname_a) VALUES (%s, %s)"
        val = actor

        cnx, cursor = self.connection()
        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record inserted.")

        actorId = cursor.lastrowid

        self.close(cnx)

        return actorId


    def insertActorFullName(self, fullName): 
        """
        Pour les actrices/acteurs qui n'ont pas un nom complet 
        du type ("prénom" "nom"), ils sont ajouté à fullname 
        pour être traiter manuelement 

        insert one Actor 

        FORMAT : (fullname_a, )

        return id of actor inserted
        FORMAT : int
        """

        sql = "INSERT INTO Actors (fullname_a) VALUES (%s)"
        val = [fullName]
        
        cnx, cursor = self.connection()
        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record inserted.")

        actorId = cursor.lastrowid

        self.close(cnx)

        return actorId


    def selectActors(self):

        """
        Select list of all actors 

        return list 
        FORMAT : [(firstname_a, lastname_a, fullname_a), (firstname_a, lastname_a, fullname_a), ....]
        """

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

    def selectActorByName(self,firstname = None, lastname = None, fullname = None):

        if not firstname and not lastname and not fullname:
            return None
        elif firstname and not lastname:
            sql = "SELECT * FROM actors WHERE firstname_a = %s"
            val = [firstname]
        elif lastname and not firstname:
            sql = "SELECT * FROM actors WHERE lastname_a = %s"
            val = [lastname]
        elif fullname:
            sql = "SELECT * FROM actors WHERE fullname_a = %s"
            val = [fullname]    
        else:
            sql = "SELECT * FROM actors WHERE firstname_a = %s and lastname_a = %s"
            val = [firstname, lastname]
        
        cnx, cursor = self.connection()

        cursor.execute(sql, val)

        actor = cursor.fetchone()

        self.close(cnx)
        
        return actor

    def selectActorsNull(self):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM actors WHERE firstname_a IS NULL"

        cursor.execute(sql)

        listActors = cursor.fetchall()

        self.close(cnx)

        return listActors

    def updateActor(self, oldName, newFirstname, newLastname):

        sql = "UPDATE actors set firstname_a = %s, lastname_a = %s WHERE fullname_a = %s"
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

    ##########################################################################################################################################
    ##########################################################################################################################################
                                                                   # Casting_With
    ##########################################################################################################################################
    ##########################################################################################################################################

    def insertCasting(self, actorId, movieId):

        sql = "INSERT INTO casting_with (id_a, id_m) VALUES (%s,%s)"
        val = (actorId, movieId)
      
        cnx, cursor = self.connection()
        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record inserted.")

        castingId = cursor.lastrowid
        
        self.close(cnx)

        return castingId


    def selectCastingById(self, castingId):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM casting_with WHERE id_w = %s"
        val = [castingId]
        
        cursor.execute(sql, val)

        castingMovie = cursor.fetchone()
        lg.info(f"{cursor.rowcount} record selected.")
        self.close(cnx)
        
        return castingMovie


    def selectCastingByActorIdMovieId(self, actorId, movieId):

        cnx, cursor = self.connection()

        sql = "SELECT * FROM casting_with WHERE id_a = %s and id_m = %s"
        val = (actorId, movieId)
        
        cursor.execute(sql, val)

        castingMovie = cursor.fetchone()
        lg.info(f"{cursor.rowcount} record selected.")
        self.close(cnx)
        
        return castingMovie

    def deleteCastingById(self, castingId):

        sql = "DELETE FROM casting_with WHERE id_w = %s"
        val = [castingId]

        cnx, cursor = self.connection()
        cursor.execute(sql, val)

        cnx.commit()

        lg.info(f"{cursor.rowcount} record deleted.")

        self.close(cnx)
    