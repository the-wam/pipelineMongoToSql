#! /usr/bin/env python3
# coding: utf-8

from src import openJson
from src.addData.moviesController import moviesController
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("-f", "--filePath", help="Json file to add")
args = parser.parse_args()



if "__main__" == __name__:

    # load data
    movies = openJson(args.filePath)

    # Data ingetion 
    moviesAdder = moviesController()
    moviesAdder.run(movies)


        



