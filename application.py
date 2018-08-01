import json
from flask import Flask, Response
from flask_restplus import Resource, Api


# welcome to flask: http://flask.pocoo.org/
# working with sqlalchemy & swagger:
# http://michal.karzynski.pl/blog/2016/06/19/building-beautiful-restful-apis-using-flask-swagger-ui-flask-restplus/
# hello world
application = Flask(__name__)
api = Api(application)
with open('pokemon.json') as json_file:
    data = json.load(json_file)


@api.route("/pokemon/<string:pokemon>")                   # Create a URL route to this resource
class Pokemon(Resource):                               # Create a RESTful resource
    def get(self, pokemon):                               # Create GET endpoint
        return data.get(pokemon)


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


@api.route("/pokemon/attacks/<int:attacks>")
class PokemonAttacks(Response):
    def get(self, attacks):
        pokemon_names = ''
        for name in data:
            if attacks == data[name]["stats"]["attacks"]:
                pokemon_names += name
                pokemon_names += ' '

'''
        pokemon_dict = {}
        for names in pokemon_names.split():
            pokemon_dict.update({names: data.get(names)})

        json_format = json.dumps(pokemon_dict)
        return Response(response=json_format, mimetype="application/json", status=200)
'''

print(PokemonAttacks().get(attacks=60))

'''
def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
'''