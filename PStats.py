import requests               #get(), format(), json()
from flask import Flask, render_template       #Flask()

app = Flask(__name__)

API_URL = 'https://api.chess.com/pub/player/{}/stats'

def query_api(name):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(API_URL.format(name), headers=headers)
    return response


def get_chess_rapid_summary(data):
    if 'chess_rapid' not in data:
        return "Rapid: No data available"

    rapid = data['chess_rapid']
    last_rating = rapid.get('last',{}).get('rating', 'N/A')
    best_rating = rapid.get('best',{}).get('rating', 'N/A')
    record = rapid.get('record',{})
    wins = record.get('win',0)
    losses = record.get('loss',0)
    draws = record.get('draw',0)

    return (  
        f"Last Rating: {last_rating}, Best Rating: {best_rating}, Record: {wins}W/{losses}L/{draws}D"
    )

def get_chess_blitz_summary(data):
    if 'chess_blitz' not in data:
        return "blitz: No data available"

    blitz = data['chess_blitz']
    last_rating = blitz.get('last',{}).get('rating', 'N/A')
    best_rating = blitz.get('best',{}).get('rating', 'N/A')
    record = blitz.get('record',{})
    wins = record.get('win',0)
    losses = record.get('loss',0)
    draws = record.get('draw',0)

    return (  
        f"Last Rating: {last_rating}, Best Rating: {best_rating}, Record: {wins}W/{losses}L/{draws}D"
    )

def get_chess_bullet_summary(data):
    if 'chess_bullet' not in data:
        return "bullet: No data available"

    bullet = data['chess_bullet']
    last_rating = bullet.get('last',{}).get('rating', 'N/A')
    best_rating = bullet.get('best',{}).get('rating', 'N/A')
    record = bullet.get('record',{})
    wins = record.get('win',0)
    losses = record.get('loss',0)
    draws = record.get('draw',0)

    return (  
        f"Last Rating: {last_rating}, Best Rating: {best_rating}, Record: {wins}W/{losses}L/{draws}D"
    )



@app.route('/player/<name>/stats')
def result(name): 
    data = query_api(name)
    if not data:
        return f"Player '{name}' not found!"
    else:
        data = data.json()
        rpdSummary = get_chess_rapid_summary(data)
        bltSummary = get_chess_bullet_summary(data)
        btzSummary = get_chess_blitz_summary(data)
        return f"Rapid: {rpdSummary}; Blitz: {btzSummary}; Bullet: {bltSummary}"
        # return f" Rapid: {data['chess_rapid']}, Blitz:{data['chess_blitz']}, Bullet:{data['chess_bullet']}"
    

if __name__ == '__main__':
    app.run(debug=True)