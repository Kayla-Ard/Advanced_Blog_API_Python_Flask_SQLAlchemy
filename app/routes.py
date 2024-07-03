from app import app 
from flask import request
from app.schemas.userSchema import user_input_schema, user_output_schema, users_schema
from app.schemas.postSchema import post_schema, posts_schema
from marshmallow import ValidationError
from app.database import db 
from app.models import User, Post
from werkzeug.security import generate_password_hash



@app.route('/')
def index():
    return 'Testing'

