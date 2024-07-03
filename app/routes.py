from app import app 
from flask import request, jsonify
from app.schemas.userSchema import user_input_schema, user_output_schema, users_schema
from app.schemas.postSchema import post_schema, posts_schema
from marshmallow import ValidationError
from app.database import db 
from app import db
from app.models import User, Post
from werkzeug.security import generate_password_hash
from app.schemas import ma


@app.route('/')
def index():
    return 'Testing'


# User Routes

# Get all users
@app.route('/users', methods=['GET'])
def get_all_users():
    query = db.select(User)
    users = db.session.execute(query).scalars().all()
    return users_schema.jsonify(users)


# Get a single user by ID
@app.route('/users/<int:user_id>', methods=["GET"])
def get_single_user(user_id):
    
    user = db.session.get(User, user_id)

    if user is not None:
        return user_output_schema.jsonify(user)
    return {"error": f"Customer with ID {user_id} does not exist"}, 404


# Create a new user
@app.route('/users', methods=["POST"])
def create_user():
    
    if not request.is_json:
        return {"error": "Request body must be application/json"}, 400 
    try:
    
        data = request.json
        
        user_data = user_input_schema.load(data)
        
        query = db.select(User).where( (User.username == user_data['username']) | (User.email == user_data['email']) )
        check_users = db.session.scalars(query).all()
        if check_users: 
            return {"error": "User with that username and/or email already exists"}, 400 
        
        new_user = User(
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            username=user_data['username'],
            email=user_data['email'],
            password=generate_password_hash(user_data['password'])
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return user_output_schema.jsonify(new_user), 201 
    except ValidationError as err:
        return err.messages, 400
    except ValueError as err:
        return {"error": str(err)}, 400
    
    
# Post Routes
    
# Get all posts
@app.route('/posts', methods=['GET'])
def get_all_posts():
    posts = db.session.query(Post).all()
    return posts_schema.jsonify(posts)


# Get a single post by ID
@app.route('/posts/<int:post_id>', methods=["GET"])
def get_single_post(post_id):
    post = db.session.query(Post).filter_by(id=post_id).first()
    if post:
        return post_schema.jsonify(post)
    return {"error": f"Post with ID {post_id} does not exist"}, 404


# Create a new post
@app.route('/posts', methods=["POST"])
def create_post():
    if not request.is_json:
        return {"error": "Request body must be application/json"}, 400 
    
    try:
        data = request.json
        post_data = post_schema.load(data)
        
        new_post = Post(
            title=post_data['title'],
            body=post_data['body'],
            user_id=post_data['user_id']
        )
        
        db.session.add(new_post)
        db.session.commit()
        
        return post_schema.jsonify(new_post), 201 
    except ValidationError as err:
        return err.messages, 400
    except Exception as e:
        return {"error": str(e)}, 500
