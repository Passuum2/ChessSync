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

# @app.route('/<name>')
# #Second route# Get column names    tGames = cur.fetchall()
#     player = player.json()
#     return f"Username: {player['username']}"

@app.route('/test')
#Index route
def champtemp():
    #champtemp():
    #Implementation: 
    dGames = getDatabase(games)
    dElo = getDatabase(elo)
    dEco = getDatabase(eco)
    return render_template('chesschamp.html', games = dGames, elo = dElo, eco = dEco)

if __name__ == '__main__':
    app.run(debug=True)
