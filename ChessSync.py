#ChessSync.py-
#Myles Darity-Reese, Sri
#18-Apr-25
#

from flask import Flask, render_template     #render_template(), run()
from flask_mysqldb import MySQL              #fetchall, fetchone(), execute(), connection.cursor(), MySQL()
from modules import query_api                #query_api()
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

@app.route('/test')
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

if __name__ == '__main__':
    app.run(debug=True)