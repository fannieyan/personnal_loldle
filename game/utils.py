import pymongo
import os

connection = pymongo.MongoClient(os.getenv("MONGODB_CONNEXION"))
db_model = connection["LoLChampionsProperties"]