from flask import Flask
from flask_restful import Api

from view import GetFormResource

app = Flask(__name__)

api = Api(app)

@app.route("/")
def main():
    return "HERE WE ARE"

api.add_resource(GetFormResource, '/get_form')

if __name__=="__main__":
    app.run(port=7777, debug=False)