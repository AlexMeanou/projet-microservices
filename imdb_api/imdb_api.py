from fastapi import FastAPI, responses
from functions import *


app = FastAPI()


@app.get('/')
async def root():
    return {"message" : "Best app ever !"}


@app.get('/proposistions')
async def movie_by_genre(id):
    res = get_movie_by_id(id=id)
    # print(res.json())
    return res.json()


@app.get('/movie/genre')
async def movie_by_genre(genre):
    res = get_movie_by_genre(genre=genre)
    # print(res.json())
    return res.json()


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
