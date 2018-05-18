from flask_restful import Resource
from db import db
from flask import request

class GetFormResource(Resource):

    def get(self):
        return "<http>WTF??? *UCK THS SHIT</http>"


    def post(self):
        s = ''
        for k, v in request.args.items():
            s += k + ' : ' + v + '\n'

        return s