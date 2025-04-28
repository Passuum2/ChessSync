#ChessSync.py-
#Myles Darity-Reese, Sri
#
from flask import Flask, render_template
from modules import query_api

app = Flask(__name__)
application = app

@app.route('/')
#Index route
def index():
    #index(): Renders index.html
    #implementation: 
    return render_template('index.html')

@app.route('/<name>')
#Second route
def search(name) -> str:
    #
    #
    
    player = query_api(name)
    if not player:
        return f"Player '{name}' not found!"

    player = player.json()
    return f"Username: {player['username']}"

if __name__ == '__main__':
    app.run(debug=True)
