# -*- coding: utf-8 -*-


import pymongo
from pymongo import MongoClient


class PyMongoDb(object):
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def insert(self, sql):
        pass

    def delete(self):
        pass

    def update(self):
        pass

    def query(self):
        pass

    def count(self):
        pass


client = MongoClient(host='192.168.99.100', port=27017, username='root', password='123456')
db = client.get_database(name='admin')
col = db.get_collection('test')
# col = db.create_collection('test1')
col.insert_one({'name': 'zhangsan', 'title': 'mongodb'})

for row in col.find():
    print(row)





