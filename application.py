
import json
from flask import Flask, Response
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import fields


# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
# hello world
application = Flask(__name__)
api = Api(application)
with open('pokemon.json') as json_file:
    data = json.load(json_file)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(application)

# pokemonhp = api.model('HP', {
# #     'pokemon': fields.String(required=True, description='Pokemon Name')
# # })


# @api.route("/pokemon/<string:pokemon>")                     # Create a URL route to this resource
# class HelloWorld(Resource):                                 # Create a RESTful resource
#     def get(self, pokemon):                                 # Create GET endpoint
#         return data.get(pokemon)
#
#
# @api.route("/pokemon/hp/<int:hp>")
# class hp(Resource):
#     def get(self, pokemon, stats, hp):
#         for key in data:
#             if data.get(pokemon.get(stats.get(hp))) == self:
#                 return key
#
@api.route("/pokemon/<string:pokemon>")                   # Create a URL route to this resource
class Pokemon(Resource):                               # Create a RESTful resource
    def get(self, pokemon):                               # Create GET endpoint
        return data.get(pokemon)


@api.route("/pokemon/hp/<int:hp>")
class PokemonHP(Resource):
    def get(self, hp):
        pokemon_names = ''
        for name in data:
            if hp == data[name]["stats"]["hp"]:
                pokemon_names += name
                pokemon_names += ' '

        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)


@api.route("/pokemon/attack/<int:attack>")
class PokemonAttack(Resource):
    def get(self, attack):
        pokemon_names = ''
        for name in data:
            if attack == data[name]["stats"]["attack"]:
                pokemon_names += name
                pokemon_names += ' '

        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)


@api.route("/pokemon/defense/<int:defense>")
class PokemonDefense(Resource):
    def get(self, defense):
        pokemon_names = ''
        for name in data:
            if defense == data[name]["stats"]["defense"]:
                pokemon_names += name
                pokemon_names += ' '

        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)


@api.route("/pokemon/special_attack/<int:special_attack>")
class PokemonSpecialAttack(Resource):
    def get(self, special_attack):
        pokemon_names = ''
        for name in data:
            if special_attack == data[name]["stats"]["special_attack"]:
                pokemon_names += name
                pokemon_names += ' '

        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)


@api.route("/pokemon/special_defense/<int:special_defense>")
class PokemonSpecialDefense(Resource):
    def get(self, special_defense):
        pokemon_names = ''
        for name in data:
            if special_defense == data[name]["stats"]["special_defense"]:
                pokemon_names += name
                pokemon_names += ' '

        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)


@api.route("/pokemon/speed/<int:speed>")
class PokemonSpeed(Resource):
    def get(self, speed):
        pokemon_names = ''
        for name in data:
            if speed == data[name]["stats"]["speed"]:
                pokemon_names += name
                pokemon_names += ' '

        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)



# print(PokemonSpecialDefense().get(special_defense=60))


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

