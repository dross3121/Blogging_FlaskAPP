# Flask app instances

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) #-->variable for databse
migrate = Migrate(app, db)

from app import routes, models