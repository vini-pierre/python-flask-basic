from src.models import db
from src.models.author import Author
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do author
###

def create(data):
    try:

        first_name = data.get('first_name')
        if not first_name:
            json_abort(400,"First Name is required")

        last_name = data.get('last_name')
        if not last_name:
            json_abort(400,"Last Name is required")

 
        author = Author(first_name=first_name,last_name=last_name)
        db.session.add(author)
        db.session.commit()

        return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        author = Author.query.filter_by(id=id).first()

        if not author:
            json_abort(400,"Author not found")
        else:
            return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        author = Author.query.filter_by(id=id).first()

        if not author:
            json_abort(400,"Author not found")
        else:

            first_name = data.get('first_name')
            if not first_name:
                json_abort(400,"First Name is required")

            last_name = data.get('last_name')
            if not last_name:
                json_abort(400,"Last Name is required")


            author.first_name = first_name
            author.last_name = last_name
            
            db.session.delete(author)
            db.session.commit()
        
            return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        author = Author.query.filter_by(id=id).first()

        if not author:
            json_abort(400,"Author not found")
        else:
            db.session.delete(author)
            db.session.commit()
        
            return author

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)