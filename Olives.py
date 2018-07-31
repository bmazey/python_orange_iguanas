import uuid
from flask import Flask, request, jsonify
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_sqlalchemy import SQLAlchemy

# simple flask application definition
application = Flask(__name__)
api = Api(application)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

'''
json marshaller (object <-> json)
'''
pokemon = api.model('pokemon', {
    'name': fields.String(required=True, description='pokemon name'),
    'stats': fields.String(required=True, description='pokemon stats'),
})

pokemon_type = api.model('pokemon_type', {
    'type': fields.String(readOnly=True, description='unique identifier of a pokemon'),
    'name': fields.String(required=True, description='pokemon name'),
})

pokemon_health = api.model('pokemon_health', {
    'health': fields.String(readOnly=True, description='unique identifier of a pokemon'),
    'name': fields.String(required=True, description='pokemon name')
})


'''
Rumor object model (Rumor <-> rumor) 
ignore warning as props will resolve at runtime
'''


class Pokemon(db.Model):
    type = db.Column(db.String(80), unique=, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<Pokemon %r>' % self.content


# def create(data):
    # id = str(uuid.uuid4())
    # name = data.get('name')
    # content = data.get('content')
    # pokemon = Pokemon(id=id, name=name, content=content)
    # db.session.add(pokemon)
    # db.session.commit()
    # return rumor


'''
API controllers
'''


@api.route("/pokemon")
class PokemonRoute(Resource):
    def get(self):
        return {'Pikachu': 'electric'}


# id is a url-encoded variable
@api.route("/pokemon/<string:type>")
class Pokemontype(Resource):
    @api.marshal_with(pokemon_type)
    # id becomes a method param in this GET
    def get(self, type):
        # use sqlalchemy to get a rumor by ID
        return Pokemon.query.filter(Pokemon.type == type)

@api.route("/pokemon/health/<string:hp>")
class PokemonHp(Resource):
    @api.marshal_with(pokemon_health)
    # id becomes a method param in this GET
    def get(self, hp):
        # use sqlalchemy to get a rumor by ID
        return Pokemon.query.filter(Pokemon.hp == hp)


'''
helper methods (for testing and sqlalchemy configuration)
'''


def configure_db():
    db.create_all()
    db.session.commit()


# for testing only!
def get_app():
    return application


def main():
    configure_db()
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
