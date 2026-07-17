import os
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)

app.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
app.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
app.config["MYSQL_CURSORCLASS"] = "DictCursor"