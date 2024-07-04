from flask_httpauth import HTTPTokenAuth
from app.utils.utils import decode_token
from app.models import User 
from app.database import db


token_auth = HTTPTokenAuth()

@token_auth.verify_token
def verify(token):
    user_id = decode_token(token)
    if user_id is not None:
        return db.session.get(User, user_id)
    else:
        return None


@token_auth.error_handler
def handle_error(status_code):
    return {"error": "Invalid token. Please try again"}, status_code