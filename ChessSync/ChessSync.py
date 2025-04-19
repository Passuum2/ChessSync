#ChessSync.py-
#Myles Darity-Reese, Sri
#

from flask import Flask, render_template
from modules import query_api

app = Flask(__name__)
application = app

@app.route('/')
#First route
def index():
    #index(): Renders index.html
    #implementation: 
    return render_template('index.html')

@app.errorhandler(404)
#Error route
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
