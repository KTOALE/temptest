from tinydb import TinyDB

db = TinyDB('templates')

if __name__=="__main__":
    db.insert({'name': 'temp1', 'fields': {'f1':'email','f2':'text'}})
    db.insert({'name': 'temp2', 'fields': {'f1':'phone','f2':'text'}})
    db.insert({'name': 'temp3', 'fields': {'f1': 'phone', 'f2': 'email'}})
    db.insert({'name': 'temp4', 'fields': {'f1': 'email', 'f2': 'email'}})
    db.insert({'name': 'temp5', 'fields': {'f1': 'phone', 'f2': 'phone'}})
    db.insert({'name': 'temp6', 'fields': {'f1': 'text', 'f2': 'text'}})
