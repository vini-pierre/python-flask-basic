from flask_restplus import fields
from src.config.restplus import api


author_request = api.model('Author Request', {
    'first_name': fields.String(required=True, description='text post') ,
    'last_name': fields.String(required=True, description='text post') 
})

author_result = api.model('Author Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'first_name': fields.String(required=True, description='text post'), 
    'last_name': fields.String(required=True, description='text post') 
})
