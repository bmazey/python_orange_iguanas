
import json
from flask import Flask, Response
from flask_restplus import Resource, Api
from flask_sqlalchemy import SQLAlchemy

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


# find pokemon data from their name
@api.route("/pokemon/<string:pokemon>")                   # Create a URL route to this resource
class Pokemon(Resource):                                  # Create a RESTful resource
    def get(self, pokemon):                               # Create GET endpoint
        return data.get(pokemon)


# find all pokemon of a certain type
@api.route("/pokemon/types/<string:types>")
class PokemonTypes(Resource):
    def get(self, types):
        pokemon_names = ''
        for name in data:
            if [types] == data[name]["types"]:
                pokemon_names += name
                pokemon_names += ' '

        # converts to json
        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)


# find all pokemon of a certain health
@api.route("/pokemon/stats/hp/<int:hp>")
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


# find all pokemon of a certain attack value
@api.route("/pokemon/stats/attack/<int:attack>")
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


# find all pokemon of a certain defense value
@api.route("/pokemon/stats/defense/<int:defense>")
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

# find all pokemon of a certain special attack value
@api.route("/pokemon/stats/special_attack/<int:special_attack>")
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


# find all pokemon of a certain special defense value
@api.route("/pokemon/stats/special_defense/<int:special_defense>")
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


# find all pokemon of a certain speed value
@api.route("/pokemon/stats/speed/<int:speed>")
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


# find all pokemon of a certain speed value
@api.route("/pokemon/stats/greater/speed/<int:speed>")
class PokemonSpeed(Resource):
    def get(self, speed):
        pokemon_names = ''
        for name in data:
            if speed <= data[name]["stats"]["speed"]:
                pokemon_names += name
                pokemon_names += ' '

        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)



def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

