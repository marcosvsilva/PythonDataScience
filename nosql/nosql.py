import datetime
from pymongo import MongoClient

conn = MongoClient('localhost', 27017)

db = conn.cadastroDB

post1 = {"codigo": "ID-12456",
         "prod_nome": "Geladeira",
         "marcas": ["Brasemp", "Consul", "Electrolux"],
         "data_cadastro": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post1)

print(post_id.inserted_id)

post2 = {"codigo": "ID-654321",
         "prod_nome": "Televisor",
         "marcas": ["Samsung", "LG", "TLC"],
         "data_cadastro": datetime.datetime.utcnow()}

collection.insert_one(post2)

for posts in collection.find():
    print(posts)

print(db.name)

print(db.collection_names())