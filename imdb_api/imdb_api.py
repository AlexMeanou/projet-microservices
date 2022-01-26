from fastapi import FastAPI, responses
from functions import *


app = FastAPI()


@app.get('/')
async def root():
    return {"message" : "Best app ever !"}


@app.get('/proposistions')
async def getRadom():
    res = testGet()
    print(res.json())
    return res.json()
