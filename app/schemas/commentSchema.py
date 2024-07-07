from app.schemas import ma
from marshmallow import fields, validate


class CommentSchema(ma.Schema):
    id = fields.Integer(required=False) 
    title = fields.String(required=True)
    user_id = fields.Float(required=True, validate=validate.Range(min=0))
    body = fields.String(required=True)

# Create an instance of the Comment Schema
comment_schema = CommentSchema()
comments_schema = CommentSchema(many=True) 