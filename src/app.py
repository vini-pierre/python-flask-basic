import os
from flask import Flask, Blueprint 
#import configuracao
from src.config.restplus import api,init_config
from src.config.settings import config_by_name 
#import databese e models
from src.models import db
from src.models.author import Author
from src.models.post import Post
#import blueprint controllers
from src.api.author_controller import ns as author_namespace
from src.api.post_controller import ns as post_namespace


   
    
def create_app(config_name):
    #inicia flask
    app = Flask(__name__)
    #inicia configuracao variaveis de ambiente
    app.config.from_object(config_by_name[config_name])

    setup_app(app)

    return app


def setup_app(app):
    # cria as tabelas se elas nao existirem ainda
    @app.before_first_request
    def create_tables():
        db.create_all()
 
    #inicia base de dados
    db.init_app(app) 

    #congirura blueprint para as rotas com namespace
    blueprint = Blueprint('api', __name__, url_prefix='/api')

    #adiciona blueprint no app 
    api.init_app(blueprint)
    #chama a funcao que vai congigurar as API
    init_config(app)
    #adiciona namespaces to blueprint
    api.add_namespace(author_namespace)
    api.add_namespace(post_namespace) 

    #registra blueprint
    app.register_blueprint(blueprint, url_prefix='')
    
    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')