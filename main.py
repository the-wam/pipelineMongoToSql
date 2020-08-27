#! /usr/bin/env python3
# coding: utf-8

from src.database import genresSql
from src import openJson


if "__main__" == __name__:

    # add config file
    config = openJson("config/config.json")

    test = genresSql(config["host"], config["user"], config["password"], config["database"], config["port"])

    if False:
        toto1 = "toto1"
        toto2 = "toto2"

        test.insertGenre(toto1)
        

        testByName = test.selectGenreByName(toto1)
        print(f"Select by name : {testByName}")
        testById = test.selectGenreById(testByName[0])
        print(f"Select by ID : {testById}")

        test.deleteGenreByName(toto1)

        print(test.selectGenres)