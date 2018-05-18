from tinydb import TinyDB

db = TinyDB('templates')

if __name__=="__main__":
    db.insert({'name':'temp1', 'fields':{'f1':'email','f2':'text'}})
    db.insert({'name':'temp2', 'fields':{'f1':'phone','f2':'text'}})
    db.insert({'name':'email', 'type':'asdasdasd'})
