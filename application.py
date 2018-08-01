import json
from flask import Flask
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
class HelloWorld(Resource):            # Create a RESTful resource
    def get(self, pokemon):                     # Create GET endpoint
        return data.get(pokemon)


@api.route("/pokemon/type/<string:types>")
class PokemonType(Resource):
    def get(self, types):
        pokemon_names = ''
        for name in data:
            if types == data[name]["types"]:
                pokemon_names += name
                pokemon_names += ' '
        return json.dumps(pokemon_names.split())


print(PokemonType().get(types=["grass"]))

#
# def main():
#     application.debug = True
#     application.run()
#
#
# if __name__ == "__main__":
#     main()
