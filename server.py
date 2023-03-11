from flask import Flask
from flask_restful import Api, Resource





app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
api.add_resource(HelloWorld, '/api/hello')


# @app.route("/")
# def context():
#     return {"A","B","C"}

if __name__ == "__main__":
    app.run(port=1001, debug=True)