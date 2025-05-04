#ChessSync.py-
#Myles Darity-Reese, Sri
#18-Apr-25
#

from flask import Flask, render_template     #render_template(), run()
from flask_mysqldb import MySQL              #fetchall, fetchone(), execute(), connection.cursor(), MySQL()
from modules import *                        #query_api()
from db import app                           #private
from queries import *                        #games, champion, elo, eco, location

mysql = MySQL(app)

def getDatabase(sqlQuery) -> tuple:
    #getDatabase():
    #Implementation:
    cur = mysql.connection.cursor()
    cur.execute(sqlQuery)
    sqlDB = cur.fetchall()
    return sqlDB

@app.route('/')
#Index route
def index():
    #index(): Renders index.html
    #Implementation: 
    return render_template('index.html')

@app.route('/<name>')
def search(name):
    player_response = query_api(name)
    if player_response is not None:
        player = player_response.json()
        return render_template('playertemp.html', player = player)
    else:
        return render_template('404.html') #TODO

@app.route('/db/championship')
#Index route
def champtemp():
    #champtemp():
    #Implementation: 
    dGames = getDatabase(games)
    dElo = getDatabase(elo)
    dEco = getDatabase(eco)
    return render_template('chesschamp.html', games = dGames, elo = dElo, eco = dEco)

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/games/<name>')
#Index route
def players(name):
    #players():
    #Implementation: 
    player_query = f"""
    SELECT 
        g.id AS game_id,
        g.white_player,
        g.black_player,
        g.result,
        c.year,
        e.moves
    FROM games g
    JOIN champion c ON g.championship_id = c.id
    LEFT JOIN eco e ON g.id = e.game_id
    WHERE g.white_player = '{name}' OR g.black_player = '{name}'
    ORDER BY c.year DESC;
    """
    dPlayer = getDatabase(player_query)
    return render_template('GMtemp.html', games = dPlayer)

@app.route('/<name>/stat')
def pstat(name):
    apiStats = query_statsapi(name)
    if apiStats is not None:
        player = apiStats.json()
        return render_template('stats.html', stats=player)
    else:
        return render_template('404.html') #TODO

if __name__ == '__main__':
    app.run(debug=True)