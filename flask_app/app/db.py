from pymongo import MongoClient


mongodb_url = "mongodb://mongo:27017/"  # URL-адрес вашей MongoDB
database_name = "mydatabase"
collection_name = "keys_kollection"

client = MongoClient(mongodb_url)

db = client[database_name]

collection = db[collection_name]
