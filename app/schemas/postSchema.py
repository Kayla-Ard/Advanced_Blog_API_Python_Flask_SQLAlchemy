from app.schemas import ma
from marshmallow import fields, validate


class PostSchema(ma.Schema):
    id = fields.Integer(required=False) 
    title = fields.String(required=True)
    user_id = fields.Float(required=True, validate=validate.Range(min=0))
    body = fields.String(required=True)

# Create an instance of the PostSchema
post_schema = PostSchema()
posts_schema = PostSchema(many=True) 