from pymongo import MongoClient

client = MongoClient('mongodb://toto:tata@localhost:27017/')

db = client.wtwt
movies = db.movies


print("zizi")
data = movies.find()
print(data)
print({"data":[ x for x in data]})
