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

@app.get("/movies/{page}")
async def get_movies_by_page(page : int):
    return [m for m in movies.find().skip(page * 10).limit(10)]

@app.get("/action_movies/{page}")
async def get_movies_by_page(page : int):
    return [m for m in movies.find().skip(page * 10).limit(10)]