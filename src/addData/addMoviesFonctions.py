import logging as lg

class AddMoviesFonctions():
    def __init__(self, movieDict):
        self.movieDict = movieDict
        self.listMovieKeys = self.movieDict.keys()
    
    def attributeValue(self, keyName):

        """
        Return the dictionary value has this key.

        Parameters:
            keyName (str) : a dictionary key

        Returns:
            int : the dictionary value has this key
            str : the dictionary value has this key
            None
        """

        if keyName in self.listMovieKeys:
            return self.movieDict[keyName]
        else:
            lg.info(f"{str(self.movieDict)} has not {keyName}")

            return None

    def checkKeyValueInt(self, keyName, listMovieKeys, movieDict):
        """
        Return the dictionary value has this key.

        Parameters:
            keyName (str) : a dictionary key, list of Keys, the dictionary of movie

        Returns:
            int : the dictionary value has this key
        """
        if keyName in listMovieKeys:
            return movieDict[keyName]
        else:
            lg.info(f"{str(movieDict)} has not {keyName}")

        return 0

    def ifNull(self, note):
        """
        Return a int value 

        Parameters:
            note : 
            
        Returns :
            int : value
        """
        if note:
            return note
        return 0