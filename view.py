import re, datetime
from flask_restful import Resource
from db import db
#from flask import request

class GetFormResource(Resource):

    EMAIL_RE = re.compile(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    PHONE_RE = re.compile(r'\+7 [0-9][0-9][0-9]'
                         r' [0-9][0-9][0-9]'
                         r' [0-9][0-9] [0-9][0-9]')
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
        return "<http>You need to use POST method</http>"


    def post(self):
        s = '@asdasdasd.com'
        return 'DB: {} && type:{}'.format(db.all(),GetFormResource.gettype(s))
