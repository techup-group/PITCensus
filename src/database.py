#!/usr/bin/env python
# Functions to handle database connections
import pymongo
from config import PitConfig

#Return the currently-used (latest) MongoDB collection
def getCurrentCollection():
    return getCollectionByYear(PitConfig['database']['pityear'])

#A an instance to a collection of surveys by year, e.g, "2017"
def getCollectionByYear(yearString):
    host = PitConfig['database']['host']
    port = int(PitConfig['database']['port'])
    client = pymongo.MongoClient(host, port)
    db = client["pit"]
    collection = db[yearString]
    return collection
