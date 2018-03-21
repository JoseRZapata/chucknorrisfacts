# -*- coding: utf-8 -*-

"""Main module
@title           : ChuckNorrisFacts
@description     : Print a random Chuck Norris Joke
@author          : Jose R. Zapata
@webpage         : joserzapata.github.io
@date            : 20 March 2018

Im using this script to learn how to make a python packages
with cookiecutter 1.6.0
https://github.com/audreyr/cookiecutter
"""
from __future__ import print_function
import json
from requests import get

def cnfacts():
    url = 'https://api.chucknorris.io/jokes/random'
    datafull = get(url).text
    info = json.loads(datafull)
    fact = info["value"]
    print("*** Chuck Norris Facts ***")
    print('\033[1;34m'+fact+'\033[0m')
    print("***")
    return None
