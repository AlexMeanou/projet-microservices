# import string
# import requests


# def get_movie_by_id(id: string):
#     return requests.get(f'https://imdb-api.com/API/Title/k_xgqcmk1o/{id}/')

# # def getMoviesListID(idList : list):
# #     res = []
# #     for id in idList:
# #         res.append(requests.get('https://imdb-api.com/API/Title/k_xgqcmk1o/{id}/'))
# #     return res

# def get_movie_by_genre(genre: list):
#     req = "https://imdb-api.com/API/AdvancedSearch/k_xgqcmk1o/?genres=" + genre
#     print (req)
#     return requests.get(req)