#search.py - Class that uses Chess.com api to search for players
#Myles Darity-Reese, Sri
#12-Apr-2025
#Functions:
#
#NOTE:CREDIT: https://support.chess.com/en/articles/9650547-published-data-api

import requests               #get(), format(), json()
from flask import Flask, render_template       #Flask()

app = Flask(__name__)

API_URL = 'https://api.chess.com/pub/player/{}'

def query_api(name):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(API_URL.format(name), headers=headers)
    return response

@app.route('/player/<name>')
def result(name):
    data = query_api(name)
    if not data:
        return f"Player '{name}' not found!"
    else:
        data = data.json()
        return f"Username: {data['username']}, Name {data['name']}"

if __name__ == '__main__':
    app.run(debug=True)