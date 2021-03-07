import mysql.connector
from mysql.connector import connect
from mysql.connector import IntegrityError
from mysql.connector import errorcode

from src import openJson
import logging as lg

# add config file
config = openJson("config/config.json")

class ConnectionSql:

    def __init__(self, host, user, password, database, port):

        self.__host__ = host
        self.__user__ = user
        self.__password__ = password
        self.__database__ = database
        self.__port__ = port

        cnx, _ = self.connection()

        self.close(cnx)



    def connection(self):
        """
            open connection
        """
        try:
            cnx = connect(
                host=self.__host__,
                user=self.__user__,
                password=self.__password__,
                port=self.__port__,
                database= self.__database__
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                lg.critical("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                lg.critical("Database does not exist")
            else:
                lg.critical(err)
        
        lg.debug("Info : connection open")

        cursor = cnx.cursor()

        return cnx, cursor

    def close(self, cnx):
        " close the connection to the database"
        cnx.close()

        lg.debug("info : connection close")

    def showDatabase(self):
        
        sql = "SHOW TABLES"

        cnx, cursor = self.connection()

        cursor.execute(sql)

        showtables = cursor.fetchall()

        self.close(cnx)

        return showtables


    def querySQL(self, query):
        
        sql = query

        cnx, cursor = self.connection()

        cursor.execute(sql)

        res = cursor.fetchall()

        self.close(cnx)

        return res