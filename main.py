#! /usr/bin/env python3
# coding: utf-8

from src import openJson
#from src.database import *
from src.addData import addMovieControler, movieGenres, moviesActors, moviesDirectors

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-f", "--filePath", help="Json file to add")
args = parser.parse_args()



if "__main__" == __name__:

    # load data
    movies = openJson(args.filePath)


    for index, movie in enumerate(movies):

        # add general informaion of movie
        movieId = addMovieControler(movie)

        # add genres
        movieGenres(movie, movieId)

        # add Actors
        moviesActors(movie, movieId)

        # add Directors
        moviesDirectors(movie, movieId)

        print(index, movie["title"])



