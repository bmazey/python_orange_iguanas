import json

import pokemon as pokemon
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
class HelloWorld(Resource):# Create a RESTful resource
    def get_db(self):


    def (self, special_attack)                     # Create GET endpoint
        return data.get(pokemon)







def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()
