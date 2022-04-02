# from functions import *
from fastapi.middleware.cors import CORSMiddleware
import requests
from tokenize import String
from fastapi import FastAPI, HTTPException, Request, Body
import sys
from pydantic import BaseModel
from pymongo import MongoClient
import os
from passlib.hash import sha256_crypt
import jwt
import itertools

from tools import jwt_auth

sys.path.append("/home/eisti/Document/ING3/projet-microservices/fast_api")
# from bdd.mongo import movies


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
groups = db.groups


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
    return {"message": "Best app ever !"}


@app.get('/movie/genre', tags=['imdb'])
async def movie_by_genre(genre, request: Request):
    res = get_movie_by_genre(genre=genre)
    error = jwt_auth(request)
    if error:
        return error
    else:
        # print(res.json())
        return res.json()


@app.get('/movie/popular', tags=['imdb'])
async def get_popular_movie(request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        res = get_popular_movies_imdb()
        return res.json()

# # @jwt_auth
# @app.get("/movies/{genre}/{page}", tags=['mongo'])
# async def get_movie_by_genre_and_page_number(genre, page:int, request: Request):
#     print('get_movie_by_genre_and_page_number')
#     # print(request)
#     error = jwt_auth(request)
#     if error:
#         return error
#     else:
#         # limite = page * 10
#         skip = page - 1
#         return [m for m in movies.find({'genres' : {'$regex': genre}}).skip(skip).limit(10)]

# genres(listgenre??) - page - isadulte(bool) - acteur(liste)?? - langue(listelangue) - notes(list[1,6])


@app.get("/movies/{genre}/{page}", tags=['mongo'])
async def get_all_movies_by_page(genre: str, page: int):
    page -= 1
    l_movies = []
    for movie in movies.find({'genres': {'$regex': genre}}).skip(page * 10).limit(10):
        if not is_enough_for_home_page(movie):
            refersh_movie_data(movie['_id'])
            new_data_movie = movies.find({"_id": movie['_id']})
            l_movies.append(new_data_movie)
        else:
            l_movies.append(movie)
    return l_movies


@app.get("/oneMovie/{movie_id}", tags=['mongo'])
async def get_one_by_id(movie_id: str, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        return [a for a in movies.find({"_id": movie_id})]


@app.get('/movie/detail/{id}', tags=['imdb'])
async def movie_by_id(id, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        res = get_movie_by_id(id=id)
        # print(res.json())
        return res.json()


@app.post('/movie/insert', tags=['mongo-test'])
async def insert_movie(data: Request):
    movie = await data.json()
    print(movie)
    insert_id = str(movies.insert_one(movie).inserted_id)
    return {"data": insert_id}


@app.get('/movie', tags=['mongo-test'])
async def get_movies():
    data = movies.find({}, {"_id": 0})
    print(list(data))
    return [x for x in movies.find({}, {"_id": 0}).limit(10)]


@app.get("/genres/", tags=['mongo'])
async def genres(request: Request):
    error = jwt_auth(request)
    # if error:
    #     return error
    # else:
    return set(list(itertools.chain(*[m['genres'].split(',') for m in movies.find({}, {"genres": 1, "_id": 0}).limit(10000)])))
    # return set(list(itertools.chain([m["genres"].split(',') for m in movies.find({},{ "genres": 1 , "_id" : 0})])))


@app.get("/borne_note/", tags=['mongo'])
async def borne_note(request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        vote = set([int(m.get('numVotes', 0)) for m in movies.find(
            {}, {"numVotes": 1, "_id": 0}).limit(100000)])
        return [min(vote), max(vote)]


@app.get("/movies/{page}/{genre}/{is_adulte}/{nb_note}/{star}", tags=['mongo'])
async def get_movie_by_genre_and_page_number(genre, page: int, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        # limite = page * 10
        skip = page - 1
        return [m for m in movies.find({'genres': {'$regex': genre}}).skip(skip).limit(10)]


@app.get("/movies/{mot_clef}", tags=['mongo'])
async def get_movie_by_genre_and_page_number(genre, page: int, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        # limite = page * 10
        skip = page - 1
        return [m for m in movies.find({'genres': {'$regex': genre}}).skip(skip).limit(10)]


@app.get("/movies/{page}")
async def get_all_movies_by_page(page: int):
    page -= 1
    l_movies = []
    for movie in movies.find().sort("averageRating").skip(page * 10).limit(10):
        if not is_enough_for_home_page(movie):
            refersh_movie_data(movie['_id'])
            new_data_movie = movies.find({"_id": movie['_id']})
            l_movies.append(new_data_movie)
        else:
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


class User(BaseModel):
    username: str
    password: str
    group: str = None


@app.post("/user/register/", tags=['user'])
async def create_user(body: User):
    hash_password = generate_hash(body.password)
    check_exist_group = groups.find_one({"name": body.group})
    check_exist_user = users.find_one({"username": body.username})
    if check_exist_user is None or len(list(check_exist_user)) < 1:

        if check_exist_group is None or len(list(check_exist_group)) < 1:
            print(
                "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
            groups.insert_one({"name": body.group, "members": [body.username]})
        else:
            myquery = {"_id": check_exist_group["_id"]}
            new_data = {"$push": {"members": body.username}}
            groups.update_one(myquery, new_data)

        res = users.insert_one({
            "username": body.username,
            "password": hash_password,
            "group": body.group
        })

        user_id = str(res.inserted_id)

        token = encode_auth_token({
            "username": body.username,
            "password": body.password,
            "user_id": user_id,
            "exp": 13717209,
        })

        return {"token": token}
    else:
        return {
            "error": {
                "code": 403,
                "message": "Ce nom d'utilisateur existe déjà"
            }
        }


@app.post("/user/login/", tags=['user'])
async def login(body: User):
    # TODO : il faut récupérer le password du user qui est le hash dans le bdd
    user = users.find_one({'username': body.username})
    # print(user["password"])
    if user:
        hash = user["password"]
        if verify_hash(body.password, hash):
            token = encode_auth_token({
                "username": body.username,
                "password": body.password,
                "user_id": str(user["_id"]),
                "exp": 13717209,
            })

            return {
                "data": {
                    "token": token,
                    'username': body.username
                }
            }
        else:
            return {
                "error": {
                    "code": 403,
                    "message": "Mot de passe incorrect"
                }
            }
    else:
        return {
            "error": {
                "code": 403,
                "message": "Username incorrect"
            }
        }


@app.get("/test")
async def callPython(username):
    like_movie("tt0000005", username)
    return {"test": "test"}


def get_movie_by_id(id: str):
    return requests.get(f'https://imdb-api.com/API/Title/k_4ja9gk6h/{id}/')


def get_movie_by_genre(genre: list):
    req = "https://imdb-api.com/API/AdvancedSearch/k_4ja9gk6h/?genres=" + genre
    print(req)
    return requests.get(req)


def get_popular_movies_imdb():
    return requests.get('https://imdb-api.com/en/API/MostPopularMovies/k_4ja9gk6h')


def refersh_movie_data(id):
    new_data = get_movie_by_id(id)
    myquery = {"_id": id}
    newvalues = {"$set": new_data.json()}
    # print(new_data.json()==)

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


# def proposition_perso(username):
#     user = users.find_one({'username': username})
#     if user:
#         genres = user["genres"]


def like_movie(movieId, username):
    movie_already_liked = users.find_one({"username" : username},)
    users.update_one({"username": username}, {"$push": {"films": movieId}})
    genre = users.find_one({"username": username}, {"genres": 1, "_id": 0})
    genreAdd = movies.find_one({"_id": movieId})["genres"]
    # print(genreAdd.split(','))
    if len(list(genre)) == 0:
        res = {}
        for x in genreAdd.split(','):
            res[x] = 1
    # print(res)
    else:
        res = genre["genres"]
        # taille = len(list(genre))
        for x in genreAdd.split(','):
            if x in res:
                for i in res.keys():
                    if x == i:
                        res[i] += 1
            else:
                res[x] = 1
    # print(res)
    # calculate_genre(username)
    users.update_one({"username": username}, {"$set": {"genres": res}})

# def updat_genres(genres):


def calculate_genre(username):
    user = users.find_one({"username": username})
    movie_list = list(user["films"])
    movies.find().limit(10)


# def getMoviesListID(idList : list):
#     res = []
#     for id in idList:
#         res.append(requests.get('https://imdb-api.com/API/Title/k_4ja9gk6h/{id}/'))
#     return res


# @app.get("/genres/")
# async def genres():
#
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
