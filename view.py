import re, datetime
from flask_restful import Resource
from db import db
from flask import request

class GetFormResource(Resource):

    EMAIL_RE = re.compile(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    PHONE_RE = re.compile(r"\s7\s[0-9][0-9][0-9]"
                          r"\s[0-9][0-9][0-9]"
                          r"\s[0-9][0-9]\s[0-9][0-9]")
    @classmethod
    def gettype(cls,s):
        type = ''
        if cls.EMAIL_RE.match(s):
            type = 'email'
        elif cls.PHONE_RE.match(s):
            type = 'phone'
        else:
            try:
                datetime.datetime.strptime(s, '%Y-%m-%d')
                type = 'date'
            except ValueError:
                type = 'text'

        return type


    def get(self):
        #+7%20916%20243%2032 % 2003
        return "<http>You need to use POST method</http>"


    def post(self):
        #print(request.args.get('c'))7... А НЕ +7...
        #[v for k, v in request.args.items()]
        return {k:GetFormResource.gettype(v) for k,v in request.args.items()}
