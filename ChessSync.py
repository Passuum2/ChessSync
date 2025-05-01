#ChessSync.py-
#Myles Darity-Reese, Sri
#
from flask import Flask, render_template
from modules import query_api
from flask_mysqldb import MySQL
from db import app
from queries import *

mysql = MySQL(app)

@app.route("/")
def games():
    cur = mysql.connection.cursor()
    #cur.execute(example_game_query)
    #rv = cur.fetchall()
    #return str(rv)

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

@app.route('/s')
#Index route
def champtemp():
    #index(): Renders index.html
    #implementation: 
    return render_template('chesschamp.html', )

@app.route('/learn')
#Learning page
def learn():
    return render_template('learn.html')






if __name__ == '__main__':
    app.run(debug=True)