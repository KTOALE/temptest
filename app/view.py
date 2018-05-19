import datetime
import re

from flask import request
from flask_restful import Resource

from db import db


class GetFormResource(Resource):

    EMAIL_RE = re.compile(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)')
    PHONE_RE = re.compile(r"\s7\s[1-9][0-9]{2}"
                          r"\s[0-9]{3}"
                          r"\s[0-9]{2}\s[0-9]{2}")
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

    @staticmethod
    def fieldsmatch(tempfields, request):
        ltf = len(tempfields.keys())
        lrtf = len(request.keys())
        result = False
        if ltf <= lrtf:
            for tf in tempfields:
                if tf in request.keys() and \
                   request.get(tf) == tempfields.get(tf):
                    result = True
                else:
                    result = False
                    break
        return result

    def get(self):
        #+7%20916%20243%2032 % 2003
        return "<http>You need to use POST method</http>"


    def post(self):
        #TODO:print(request.args.get('c'))7... А НЕ +7...
        result = {k:GetFormResource.gettype(v) for k,v in request.args.items()}
        for i in db.all():
            if GetFormResource.fieldsmatch(i.get('fields'), result):
                result = i.get('name')
                break
        return result
