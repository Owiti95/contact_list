# this config.py contains the main configuration of our application

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# allows as to send a request to this backend from another URL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# instance of the database gives as access to the mydatabase.db so that we can CRUD
db = SQLAlchemy(app)
