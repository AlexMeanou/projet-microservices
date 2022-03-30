# from functions import *
from tokenize import String
from fastapi import FastAPI, Request, responses
import sys
from pymongo import MongoClient
import os

sys.path.append("/home/eisti/Document/ING3/projet-microservices/fast_api")
import requests
# from bdd.mongo import movies

 
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {
        "name": "informations",
        "description": "Bienvenue sur le site de moi et moi meme",
    },
    {
        "name": "movie-genre",
        "description": "Voir tous les genres de films disponible."
    },
    {
        "name": "movie-popular",
        "description": "Voir tous les films les plus populaires ."
    },
    {
        "name": "movies-genre-page",
        "description": "Truc"
    },
]

client = MongoClient()

try:
    MONGO_URL = os.environ['MONGODB_CONNSTRING']    
    # MONGO_URL = "mongodb://toto:tata@localhost:27017/"

    client = MongoClient(MONGO_URL)
    print("BDD OK !", MONGO_URL)
except KeyError as e:
    print(e)
    pass

db = client.wtwt
movies = db.movies
people = db.people



app = FastAPI(openapi_tags=tags_metadata)

origins = [
    "http://localhost:8080/"
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"] 
)

@app.get('/', tags=['informations'])
async def root():
    return {"message" : "Best app ever !"}


@app.get('/movie/genre', tags=['movie-genre'])
async def movie_by_genre(genre):
    res = get_movie_by_genre(genre=genre)
    # print(res.json())
    return res.json()

@app.get('/movie/popular', tags=['movie-popular'])
async def get_popular_movie():
    res = get_popular_movies_imdb()
    return res.json()

@app.get("/movies/{genre}/{page}", tags=['movies-genre-page'])
async def get_movie_by_genre_and_page_number(genre, page:int):
    # limite = page * 10
    skip = page - 1
    return [m for m in movies.find({'genres' : {'$regex': genre}}).skip(skip).limit(10)]

@app.get("/oneMovie/{movie_id}")
async def get_one_by_id(movie_id: str):
    return [ a for a in movies.find({"_id" : movie_id})]

@app.get('/movie/detail/{id}')
async def movie_by_id(id):
    res = get_movie_by_id(id=id)
    # print(res.json())
    return res.json()

@app.post('/movie', tags=['movie'])
async def insert_movie(data : Request):
    movie = await data.json()
    print(movie)
    insert_id = str(movies.insert_one(movie).inserted_id)
    return {"data":insert_id}

@app.get('/movies', tags=['movies'])
async def get_movies():
    data = movies.find({},{"_id" : 0})
    print(list(data))
    return [x for x in movies.find({},{"_id" : 0}).limit(10)]


@app.get("/genres/")
async def genres():
    import itertools
    return len(set(list(itertools.chain(*[ m['genres'].split(',') for m in movies.find({},{ "genres": 1 , "_id" : 0}).limit(100000)]))))
    # return set(list(itertools.chain([m["genres"].split(',') for m in movies.find({},{ "genres": 1 , "_id" : 0})])))

@app.get("/borne_note/")
async def borne_note():
    import itertools
    vote = set([int(m.get('numVotes', 0)) for m in movies.find({},{ "numVotes": 1 , "_id" : 0}).limit(100000)])
    return [min(vote), max(vote)]
    

@app.get("/movies/{page}/{genre}/{is_adulte}/{nb_note}/{star}")
async def get_movie_by_genre_and_page_number(genre, page:int):
    # limite = page * 10
    skip = page - 1
    return [m for m in movies.find({'genres' : {'$regex': genre}}).skip(skip).limit(10)]

@app.get("/movies/{mot_clef}")
async def get_movie_by_genre_and_page_number(genre, page:int):
    # limite = page * 10
    skip = page - 1
    return [m for m in movies.find({'genres' : {'$regex': genre}}).skip(skip).limit(10)]


@app.get("/movies/{page}")
async def get_all_movies_by_page(page : int):
    page -= 1
    l_movies = []
    for movie in movies.find().sort("averageRating").skip(page * 10).limit(10):
        if not is_enough_for_home_page(movie): 
            refersh_movie_data(movie['_id'])
            new_data_movie = movies.find({"_id" : movie['_id']})
            l_movies.append(new_data_movie)
        else : 
            l_movies.append(movie)
    return l_movies

# @app.get("/movies/{genre}/{page}")
# async def get_all_movies_by_page(genre : str, page : int):
#     page -= 1
#     l_movies = []
#     for movie in movies.find().skip(page * 10).limit(10):
#         if not is_enough_for_home_page(movie): 
#             refersh_movie_data(movie['_id'])
#             new_data_movie = movies.find({"_id" : movie['_id']})
#             l_movies.append(new_data_movie)
#         else : 
#             l_movies.append(movie)
#     return l_movies



def get_movie_by_id(id: str):
        return requests.get(f'https://imdb-api.com/API/Title/k_xgqcmk1o/{id}/')

def get_movie_by_genre(genre: list):
    req = "https://imdb-api.com/API/AdvancedSearch/k_xgqcmk1o/?genres=" + genre
    print (req)
    return requests.get(req)


def get_popular_movies_imdb():
    return requests.get('https://imdb-api.com/en/API/MostPopularMovies/k_xgqcmk1o')


def refersh_movie_data(id): 
    new_data = get_movie_by_id(id)
    myquery = { "_id": id }
    print(new_data)
    newvalues = { "$set": new_data.json() }
    movies.update_one(myquery, newvalues)

def is_enough_for_home_page(data): 
    image = data.get("image", None) != None
    return image


# def getMoviesListID(idList : list):
#     res = []
#     for id in idList:
#         res.append(requests.get('https://imdb-api.com/API/Title/k_xgqcmk1o/{id}/'))
#     return res



# @app.get("/genres/")
# async def genres():
#     import itertools
#     print(set(list(itertools.chain([m["genres"] for m in movies.find({},{ "genres": 1 , "_id" : 0}).limit(10)]))))
#     # return set(list(itertools.chain([m["genres"].split(',') for m in movies.find({},{ "genres": 1 , "_id" : 0})])))




# @app.get('/listMovies')
# async def test():
#     res = getMoviesListID([
#         "tt0000011",
#         "tt0000012",
#         "tt0000013",
#         "tt0000016",
#         "tt0000017",
#         "tt0000018",
#         "tt0000019",
#         "tt0000020",
#         "tt0000015",
#         "tt0000023"
#         ]
#         )
#     return res.json()
