# from functions import *
from tokenize import String
from fastapi import FastAPI, Request
import sys
from pydantic import BaseModel
from pymongo import MongoClient
import os
from passlib.hash import sha256_crypt
import jwt

from tools import jwt_auth

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
        "name": "mongo",
        "description": "On tape sur la bdd"
    },
    {
        "name": "imdb",
        "description": "On tape sur l'api IMDB"
    },
    {
        "name": "mongo-test",
        "description": "Entrainement et test sur mongo"
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
users = db.users



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


@app.get('/movie/genre', tags=['imdb'])
async def movie_by_genre(genre):
    res = get_movie_by_genre(genre=genre)
    # print(res.json())
    return res.json()

@app.get('/movie/popular', tags=['imdb'])
async def get_popular_movie():
    res = get_popular_movies_imdb()
    return res.json()

# @jwt_auth
@app.get("/movies/{genre}/{page}", tags=['mongo'])
async def get_movie_by_genre_and_page_number(genre, page:int, request: Request):
    print('get_movie_by_genre_and_page_number')
    # print(request)
    error = jwt_auth(request)
    if error:
        return error
    else:
        # limite = page * 10
        skip = page - 1
        return [m for m in movies.find({'genres' : {'$regex': genre}}).skip(skip).limit(10)]

@app.get("/oneMovie/{movie_id}", tags=['mongo'])
async def get_one_by_id(movie_id: str):
    return [ a for a in movies.find({"_id" : movie_id})]

@app.get('/movie/detail/{id}', tags=['imdb'])
async def movie_by_id(id):
    res = get_movie_by_id(id=id)
    # print(res.json())
    return res.json()

@app.post('/movie/insert', tags=['mongo-test'])
async def insert_movie(data : Request):
    movie = await data.json()
    print(movie)
    insert_id = str(movies.insert_one(movie).inserted_id)
    return {"data":insert_id}

@app.get('/movie', tags=['mongo-test'])
async def get_movies():
    data = movies.find({},{"_id" : 0})
    print(list(data))
    return [x for x in movies.find({},{"_id" : 0}).limit(10)]


@app.get("/genres/", tags=['mongo'])
async def genres():
    import itertools
    return len(set(list(itertools.chain(*[ m['genres'].split(',') for m in movies.find({},{ "genres": 1 , "_id" : 0}).limit(100000)]))))
    # return set(list(itertools.chain([m["genres"].split(',') for m in movies.find({},{ "genres": 1 , "_id" : 0})])))

@app.get("/borne_note/", tags=['mongo'])
async def borne_note(req : Request):
    is_autorized = verify_token(req)
    if is_autorized:
        import itertools
        vote = set([int(m.get('numVotes', 0)) for m in movies.find({},{ "numVotes": 1 , "_id" : 0}).limit(100000)])
        return [min(vote), max(vote)]
    

@app.get("/movies/{page}/{genre}/{is_adulte}/{nb_note}/{star}", tags=['mongo'])
async def get_movie_by_genre_and_page_number(genre, page:int):
    # limite = page * 10
    skip = page - 1
    return [m for m in movies.find({'genres' : {'$regex': genre}}).skip(skip).limit(10)]

@app.get("/movies/{mot_clef}", tags=['mongo'])
async def get_movie_by_genre_and_page_number(genre, page:int):
    # limite = page * 10
    skip = page - 1
    return [m for m in movies.find({'genres' : {'$regex': genre}}).skip(skip).limit(10)]

class User(BaseModel):
    username : str
    password : str

@app.post("/user/register/", tags=['user'])
async def create_user(body: User):
    hash_password = generate_hash(body.password)
    res = users.insert_one({
        "username" : body.username,
        "password" : hash_password,
    })

    user_id = str(res.inserted_id) 


    token = encode_auth_token({
        "username": body.username,
        "password": body.password,
        "user_id": user_id
    })

    return {"token" : token}

@app.post("/user/login/", tags=['user'])
async def login(body: User):
    user = users.find_one({'username':body.username}) # TODO : il faut récupérer le password du user qui est le hash dans le bdd
    # print(user["password"])
    if user:
        hash = user["password"]
        if verify_hash(body.password, hash):
            token = encode_auth_token({
                "username": body.username,
                "password": body.password,
                "user_id": str(user["_id"])
            })

            return {
                "data": {
                    "token" : token
                }
            }
        else:
            return {
                "error" : {
                    "code" : 403,
                    "message" : "Mot de passe incorrect"
                }
            }
    else:
        return {
                "error" : {
                    "code" : 403,
                    "message" : "Username incorrect"
                }
            }



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

def encode_auth_token(payload):
    """
    Generates the Auth Token
    :return: string
    """

    return jwt.encode(
        payload,
        'zefjzef3421Rhréhdzjefd34é',
        algorithm='HS256'
    )

def generate_hash(password):
    return sha256_crypt.hash(password)    

def verify_hash(password, hash):
    return sha256_crypt.verify(password, hash)

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


# @app.get("/movies/{page}")
# async def get_all_movies_by_page(page : int):
#     page -= 1
#     l_movies = []
#     for movie in movies.find().sort("averageRating").skip(page * 10).limit(10):
#         if not is_enough_for_home_page(movie): 
#             refersh_movie_data(movie['_id'])
#             new_data_movie = movies.find({"_id" : movie['_id']})
#             l_movies.append(new_data_movie)
#         else : 
#             l_movies.append(movie)
#     return l_movies

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