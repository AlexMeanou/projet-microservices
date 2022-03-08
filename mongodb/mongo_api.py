from tokenize import String
from fastapi import FastAPI, responses
from pymongo import MongoClient
import datetime
import pprint


client = MongoClient()
db = client.wtwt
movies = db.movies
people = db.people


app = FastAPI()

@app.get('/')
async def root():
    return {"message" : "licorne"}

@app.get("/oneMovie/{movie_id}")
async def get_one_by_id(movie_id: str):
    return [ a for a in movies.find({"_id" : movie_id})]

@app.get("/movies")
async def get_movies_order_by_date():
    print(movies.find().sort({ "startYear" : -1 } ).next())
    return  movies.find().sort({ "startYear" : -1 } ).next()

