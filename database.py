#!/usr/bin/env python
# Functions to handle database connections
import pymongo

#Return the currently-used (latest) MongoDB collection
def getCurrentCollection():
    return getCollectionByYear("2017")

#A an instance to a collection of surveys by year, e.g, "2017"
def getCollectionByYear(yearString):
    client = pymongo.MongoClient('localhost', 27017)
    db = client["pit"]
    collection = db[yearString]
    return collection
