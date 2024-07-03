import os
from flask import Flask 
from app.database import db, migrate 



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db.init_app(app)

migrate.init_app(app, db)

from . import routes, models