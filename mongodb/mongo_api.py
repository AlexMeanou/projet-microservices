from tokenize import String
from fastapi import FastAPI, responses
from pymongo import MongoClient
import sys
sys.path.append("/home/eisti/Document/ING3/projet-microservices")
from imdb_api.functions import get_movie_by_id


client = MongoClient()
db = client.wtwt
movies = db.movies
people = db.people

app = FastAPI()

def refersh_movie_data(id): 
    new = get_movie_by_id(id)
    myquery = { "_id": id }
    newvalues = { "$set": new.json() }
    movies.update_one(myquery, newvalues)

def is_enough_for_home_page(data): 
    image = data.get("image", None) != None
    return image

@app.get('/')
async def root():
    return {"message" : "licorne"}

@app.get("/oneMovie/{movie_id}")
async def get_one_by_id(movie_id: str):
    return [ a for a in movies.find({"_id" : movie_id})]

@app.get("/movies/{page}")
async def get_movies_by_page(page : int):
    l_movies = []
    for movie in movies.find().skip(page * 10).limit(10):
        if not is_enough_for_home_page(movie): 
            refersh_movie_data(movie['_id'])
            new_data_movie = movies.find({"_id" : movie['id']})
            l_movies.append(new_data_movie)
        else : 
            l_movies.append(movie)
    return l_movies

