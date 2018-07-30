from flask import Flask
from flask_restplus import Resource, Api
import requests
import json


application = Flask(__name__)
api = Api(application)


@api.route("/hello")
class HelloWorld(Resource):            # Create a RESTful resource
    def get(self):                     # Create GET endpoint
        return {'hello': 'world'}


def main():
    application.debug = True
    application.run()


if __name__ == "__main__":
    main()

    def apple_sauce():
        r = requests.get('https://jobs.search.gov/jobs/search.json?query=nursing+jobs+with+veterans+affairs+in+albany+ny')
        return json.loads(r).text
