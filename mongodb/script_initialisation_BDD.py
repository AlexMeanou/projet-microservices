from pymongo import MongoClient
import click
import os
import csv 

@click.command()
@click.option('--name_file', default="data/dataName.tsv", help='file dataName.tsv on IMdb dataset')
@click.option('--basics_file', default="data/dataBasics.tsv", help='file dataBasics.tsv on IMdb dataset')
@click.option('--principals_file', default="data/dataPrincipals.tsv", help='file dataPrincipals.tsv on IMdb dataset')
@click.option('--ratings_file', default="data/dataRatings.tsv", help='file dataRaitings.tsv on IMdb dataset')
@click.option('--database', default="WTWT", help='name of the batabase')

def import_all(name_file, basics_file, principals_file, ratings_file, database): 
    import_data(name_file, basics_file, principals_file, database)
    import_rating(ratings_file)

def import_data(name_file, basics_file, principale_file, database):

    com = f"sed -i 's/nconst/_id/g' {name_file}"
    os.system(com)
    com = f"mongoimport --db {database} --collection people --type tsv --file {name_file} --headerline"
    os.system(com)

    com = f"sed -i 's/tconst/_id/g' {basics_file}"
    os.system(com)
    com = f"mongoimport --db {database} --collection movies --type tsv --file {basics_file} --headerline"
    os.system(com)

    com = f"mongoimport --db {database} --collection link_people_movies --type tsv --file {principale_file} --headerline"
    os.system(com)
    
def import_rating(ratings_file): 
    client = MongoClient()
    db = client.WTWT
    movies = db.movies

    read_tsv = csv.reader(open(ratings_file), delimiter="\t")

    for line in read_tsv: 
        myquery = { "_id": line[0] }
        newvalues = { "$set": { "averageRating": line[1], "numVotes" : line[2]} }
        movies.update_one(myquery, newvalues)

if __name__ == '__main__':
    import_all()

