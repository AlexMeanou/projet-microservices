# from functions import *
from array import array
from multiprocessing.dummy import Array
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

# try:
#     # MONGO_URL = os.environ['MONGODB_CONNSTRING']
#     # MONGO_URL = "mongodb://toto:tata@localhost:27017/"

#     client = MongoClient()
#     print("BDD OK !", )
# except KeyError as e:
#     print(e)
#     pass

db = client.wtwt
movies = db.movies
people = db.pepole  # en local mettre pepole de mon coté car faute dans le script d'init au départ, mais ca a déjà ete corrigé
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

# genres - page - isadulte(bool) - acteur - notes(list[1,6]) - date


@app.get("/movies/notes/{notes}/{page}")
async def get_movies_by_notes(notes, page: int):
    # print(notes[1])
    # print(notes[3])
    return [m for m in movies.find({'averageRating': {'$gte': notes[1], '$lte': notes[3]}}).skip(page * 10).limit(10)]
    # return [m for m in movies.find({ '$expr': { '$gt': [{ '$toDouble': "$averageRating" }, notes[1]] } }).limit(5)]


@app.get("/movies/adult/{page}")
async def get_movies_for_adult_audience(page: int):
    return [m for m in movies.find({'isAdult': {'$eq': 1}}).skip(page * 10).limit(10)]


# Route qui renvoie les films ayant dans leur actorList l'acteur recherché
@app.get("/movies/acteurs/{acteur}")
async def get_movies_by_actors(acteur):
    return [m for m in movies.find({'actorList.name': {'$regex': acteur}}).limit(10)]


# Route qui renvoie une liste de films dans laquelle l'acteur joue (on peut les récup sur le front et ensuite appeler le get_movie_by_id pour les id recup)
# resor les films et pas leurment les id !!!! GOOD
@app.get("/movies/people/{acteur}")
async def get_movies_from_actors(acteur):
    list_films = people.find_one({'primaryName': acteur})["knownForTitles"]
    l_movies = []
    for x in list_films.split(','):
        l_movies.append(movies.find_one({'_id': x}))
    return l_movies


@app.get("/movies/group/{name}")  # J'ai pas eu le temps de vraiment la tester comme il faudrait, ma bdd est pas comme il faut la avec tout les tests que je fais, ça marche pour un user et surement pour les groups de base mais seulement si tout le monde a au moins like un films en fait, si jamais ca retourne vide je sais pas si ca va marcher
async def get_movies_liked_by_group(name):
    users_group = list(groups.find_one({'name': name})["members"])
    movies_liked = []
    for x in range(len(users_group)):
        # print(users_group[x])
        data = users.find_one({"username": users_group[x]})
        if data.get("liked_movies", None) != None:
            for x in data["liked_movies"]:
                movies_liked.append(x)
            l_movies = []
            for x in set(movies_liked):
                l_movies.append(movies.find_one({'_id': x}))
    return l_movies
    # print(movies_liked)


@app.post("/movies/liked/{username}/{movie_id}")
async def like_a_movie(username, movie_id):
    return like_movie(movie_id, username)


@app.get("/movies/{genre}/{actor}/{notes_inf}/{notes_sup}/{search}/{page}", tags=['mongo'])
async def get_all_movies_by_page(genre: str, notes_inf: float, notes_sup: float,  actor: str, search: str, page: int):
    page -= 1
    l_movies = []
    find_list = []
    if genre != 'all':
        find_list.append({'genres': {'$regex': genre}})
    # if genre != ''
    # if actor != 'nulle':
    #     # find_list.append(f"{'genres': {'$regex': {genre}}}")
    #     pass
    # if search != 'nulle':
    #     # todo
    #     find_list.append(f"{{'genres': {{'$regex' : {genre}}}}}")
    # find_list.append(
    #     {'averageRating': {'$gte': str(int(notes_inf)), '$lte': str(int(notes_sup))}})
    # print("================================================")
    # print(f"/movies/{genre}/{actor}/{notes_inf}/{notes_sup}/{search}/{page}")
    # print({'$and': find_list})
    # print("================================================")
    if len(find_list) > 0:
        res = {'$and': [find_list]}
    else:
        res = None
    for movie in movies.find(res).skip(page * 10).limit(10):
        if not is_enough_for_home_page(movie):
            refersh_movie_data(movie['_id'])
            new_data_movie = movies.find({"_id": movie['_id']})
            l_movies.append(new_data_movie)
        else:
            l_movies.append(movie)
    return l_movies

# une route qui donne les films que le group a liké

# une route qui se base sur les preferense des utilisateur et resort une liste de film qui peuvent leurs plaire


@app.get("/movies/personnalized/{username}")
async def get_movies_based_on_preference(username):
    data = calculate_genre(username)
    print(data[0])
    test = movies.find({"$and": [{"genres": {"$regex": data[0]}}, {
                       "genres": {"$regex": data[1]}}]}).limit(10)
    return [x for x in test]


@ app.get("/oneMovie/{movie_id}", tags=['mongo'])
async def get_one_by_id(movie_id: str, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        return [a for a in movies.find({"_id": movie_id})]


@ app.get('/movie/detail/{id}', tags=['imdb'])
async def movie_by_id(id, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        res = get_movie_by_id(id=id)
        # print(res.json())
        return res.json()


@ app.post('/movie/insert', tags=['mongo-test'])
async def insert_movie(data: Request):
    movie = await data.json()
    print(movie)
    insert_id = str(movies.insert_one(movie).inserted_id)
    return {"data": insert_id}


@ app.get('/movie', tags=['mongo-test'])
async def get_movies():
    data = movies.find({}, {"_id": 0})
    print(list(data))
    return [x for x in movies.find({}, {"_id": 0}).limit(10)]


@ app.get("/genres/", tags=['mongo'])
async def genres(request: Request):
    error = jwt_auth(request)
    # if error:
    #     return error
    # else:
    tmp = set(list(itertools.chain(*[m['genres'].split(',')
              for m in movies.find({}, {"genres": 1, "_id": 0}).limit(10000)])))
    tmp = list(set([g.replace(" ", "") for g in tmp]))
    tmp.insert(0, "all")
    return tmp
    # return set(list(itertools.chain([m["genres"].split(',') for m in movies.find({},{ "genres": 1 , "_id" : 0})])))


@ app.get("/borne_note/", tags=['mongo'])
async def borne_note(request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        vote = set([int(m.get('numVotes', 0)) for m in movies.find(
            {}, {"numVotes": 1, "_id": 0}).limit(100000)])
        return [min(vote), max(vote)]


@ app.get("/movies/{page}/{genre}/{is_adulte}/{nb_note}/{star}", tags=['mongo'])
async def get_movie_by_genre_and_page_number(genre, page: int, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        # limite = page * 10
        skip = page - 1
        return [m for m in movies.find({'genres': {'$regex': genre}}).skip(skip).limit(10)]


@ app.get("/movies/{mot_clef}", tags=['mongo'])
async def get_movie_by_genre_and_page_number(genre, page: int, request: Request):
    error = jwt_auth(request)
    if error:
        return error
    else:
        # limite = page * 10
        skip = page - 1
        return [m for m in movies.find({'genres': {'$regex': genre}}).skip(skip).limit(10)]


@ app.get("/movies/{page}")
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


@ app.post("/user/register/", tags=['user'])
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


@ app.post("/user/login/", tags=['user'])
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


@ app.get("/test")
async def callPython(username):
    # return like_movie("tt0000014", username)
    return calculate_genre(username)


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
    check = True
    movie_already_liked = users.find_one(
        {"username": username}, {"liked_movies": 1, "_id": 0})
    if len(list(movie_already_liked)) == 0:
        users.update_one({"username": username}, {
                         "$push": {"liked_movies": movieId}})
    else:
        test = movie_already_liked["liked_movies"]
        for x in test:
            if x == movieId:
                check = False

    if check:
        users.update_one({"username": username}, {
                         "$push": {"liked_movies": movieId}})

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
        return res
    else:
        return {"error": "Vous avez déjà aimé ce film"}

# def updat_genres(genres):


def calculate_genre(username):
    user = users.find_one({"username": username})
    if user.get("genres", None) != None:
        userRes = user["genres"]
        most_viewed_genre = sorted(userRes, key=userRes.get, reverse=True)
        return most_viewed_genre[:2]
    else:
        return {"Error": "L'user n'a pas encore like de films"}
    # list_genre = user.split(',')
    # movies.find().limit(10)
    # print(most_viewed_genre)
    # print(x)
    # print(user[x])
    # tt.append(user[x])


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
