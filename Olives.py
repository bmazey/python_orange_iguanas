from flask import Flask
from flask_restplus import Resource, Api

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
