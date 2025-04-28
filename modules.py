#modules.py - General Useful Functions used in ChessSync Flask App
#Myles Darity-Reese, Sri
#12-Apr-2025
#Functions:
#query_api(): Returns API database

import requests      #get()

ip_adress = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
API_URL = 'https://api.chess.com/pub/player/{}'

def query_api(name):
    #query_api(): Returns API database
    #Implementation: TODO
    #NOTE:CREDIT: https://support.chess.com/en/articles/9650547-published-data-api
    response = requests.get(API_URL.format(name), headers=ip_adress)
    return response

