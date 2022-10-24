from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.author_serializer import author_request, author_result
from src.services.author_service import create, change, delete, get
 

ns = api.namespace('api/author', description='Operations related to author')

 
@ns.route('')#define rota
class AuthorCollection(Resource):
    @api.expect(author_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(author_result)#define resultado da metodo 
    def post(self):
        """
        Create a new Author
        """ 
        author = create(request.json)
        return author 

 

@ns.route('/<int:id>')
class AuthorIDCollection(Resource): 
    @api.marshal_with(author_result)
    def get(self, id):
        """
        Get author by ID
        """ 
        author = get(id)
        return author 


    @api.expect(author_request)
    @api.marshal_with(author_result)
    def put(self, id):
        """
        Change author by ID
        """ 
        author = change(id,request.json)
        return author 
 
    @api.marshal_with(author_result)
    def delete(self, id):
        """
        Delete author by ID
        """ 
        author = delete(id)
        return author 