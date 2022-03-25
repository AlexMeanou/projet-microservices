from pymongo import MongoClient
import os

client = MongoClient()

try:
    MONGO_URL = os.environ['MONGODB_CONNSTRING']
    client = MongoClient(MONGO_URL)
except KeyError:
    pass


db = client.wtwt
movies = db.movies
people = db.people

