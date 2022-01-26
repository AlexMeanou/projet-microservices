from fastapi import FastAPI, responses
from pymongo import MongoClient
import datetime
import pprint


client = MongoClient()
db = client.WTWT
movies = db.movies
people = db.people


app = FastAPI()

@app.get('/')
async def root():
    return {"message" : "licorne"}


@app.get('/oneMovie')
async def getRadom():
    return movies.find_one()

