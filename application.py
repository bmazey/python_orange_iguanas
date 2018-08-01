
import json
from flask import Flask
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

@api.route("/pokemon/<string:pokemon>")                     # Create a URL route to this resource
class HelloWorld(Resource):                                 # Create a RESTful resource
    def get(self, pokemon):                                 # Create GET endpoint
        return data.get(pokemon)


# @api.route("/pokemon/hp/<int:hp>")
# class hp(Resource):
#     def get(self, pokemon, stats, hp):
#         for key in data:
#             if data.get(pokemon.get(stats.get(hp))) == self:
#                 return key
#

def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

