# Libraries
from multiprocessing.pool import ThreadPool
from pymongo import MongoClient
from urllib import request
import shutil
import gzip
import csv
import re
import os


def download_files(path = "tmp"):
    
    os.mkdir('tmp')

    def download_url(url):
        # Download process
        print("downloading: ",url)
        file_title = re.split(pattern='/', string=url)[-1]
        urlrtv = request.urlretrieve(url=url, filename=os.path.join(path, file_title))

        # for ".tsv" to ".csv"
        title = re.split(pattern=r'\.tsv', string=file_title)[0] +".tsv"

        # Unzip ".gz" file
        with gzip.open(os.path.join(path, file_title), 'rb') as f_in:
            with open(os.path.join(path, title), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    # URL List
    urls = ["https://datasets.imdbws.com/title.ratings.tsv.gz"
            ,"https://datasets.imdbws.com/title.basics.tsv.gz"
            ,"https://datasets.imdbws.com/title.principals.tsv.gz"
            ,"https://datasets.imdbws.com/name.basics.tsv.gz"
            ]

    res = ThreadPool(len(urls)).imap_unordered(download_url, urls)
    
    count = 0
    for r in res:
        print(f"{count}/{len(urls)}")
        count += 1 

def import_rating(ratings_file): 
    client = MongoClient()
    db = client.wtwt
    movies = db.movies

    read_tsv = csv.reader(open(ratings_file), delimiter="\t")

    # TODO marqueur visuel pour connaitre le temps 
    for line in read_tsv: 
        myquery = { "_id": line[0] }
        newvalues = { "$set": { "averageRating": line[1], "numVotes" : line[2]} }
        print(myquery, newvalues)
        movies.update_one(myquery, newvalues)

def import_files_in_mongodb(path = "tmp", database = 'wtwt'):
    
    def import_tsv_mongodb(name_file, collection_name, remplace = False, el = []):
        if remplace : 
            com = f"sed -i 's/{el[0]}/{el[1]}/g' {name_file}"
            os.system(com)
        com = f"mongoimport --db {database} --collection {collection_name} --type tsv --file {name_file} --headerline"
        os.system(com)
    
    import_tsv_mongodb(os.path.join(path, "name.basics.tsv"), "pepole", remplace=True, el= ["nconst", "_id"])
    import_tsv_mongodb(os.path.join(path, "title.basics.tsv"), "movies", remplace=True, el= ["tconst", "_id"])
    import_tsv_mongodb(os.path.join(path, "title.principals.tsv"), "link_people_movies")
    
    import_rating(os.path.join(path, "title.ratings.tsv"))

def delete_files(path = "tmp"):
    try:
        shutil.rmtree(path)
    except:
        print('Error deleting directory')

if __name__ == '__main__':
    download_files()
    import_files_in_mongodb()
    delete_files()
