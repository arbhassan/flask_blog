from flask import Flask
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config["SECRET_KEY"] = "3a9bfdc8a927f9e656c54d8f06a43132"
APP.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(APP)

from flaskblog import routes
