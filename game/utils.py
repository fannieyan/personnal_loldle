import json
import pymongo
import os
from bson import json_util

connection = pymongo.MongoClient(os.getenv("MONGODB_CONNEXION"))
db_model = connection["LoLChampionsProperties"]

## Parse data sent back from MongoDB to JSON.
def parse_json(data):
    return json.loads(json_util.dumps(data))