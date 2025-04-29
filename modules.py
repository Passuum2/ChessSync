#modules.py - General Useful Functions used in ChessSync Flask App
#Myles Darity-Reese, Sri
#12-Apr-2025
#Functions:
#query_api(): Returns API database

import requests      #get()

IP_ADDRESS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
API_URL = 'https://api.chess.com/pub/player/{}'

def query_api(sName) -> requests.Response:
    #query_api(): Returns API database as request
    #Implementation: TODO
    #NOTE:CREDIT: https://support.chess.com/en/articles/9650547-published-data-api
    rReturn = requests.get(API_URL.format(sName), headers=IP_ADDRESS)
    return rReturn

