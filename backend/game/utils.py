import json
import pymongo
import os
from bson import json_util

connection = pymongo.MongoClient(os.getenv("MONGODB_CONNEXION"))
db_model = connection["LoLChampionsProperties"]

# Parse data sent back from MongoDB to JSON.


def parse_json(data):
    return json.loads(json_util.dumps(data))


lookup_all_properties = [
    {"$lookup": {
        "from": "champion_properties",
        "localField": "champion_id",
        "foreignField": "champion_id",
        "as": "properties"
    }},
    {"$unwind": "$properties"},
    {"$lookup": {
        "from": "sex",
        "localField": "properties.sex_id",
        "foreignField": "sex_id",
        "as": "sex"
    }},
    {"$lookup": {
        "from": "clan",
        "localField": "properties.clan_ids",
        "foreignField": "clan_id",
        "as": "clan"
    }},
    {"$lookup": {
        "from": "lane",
        "localField": "properties.lane_ids",
        "foreignField": "lane_id",
        "as": "lane"
    }},
    {"$lookup": {
        "from": "range",
        "localField": "properties.range_ids",
        "foreignField": "range_id",
        "as": "range"
    }},
    {"$lookup": {
        "from": "ressource",
        "localField": "properties.ressource_id",
        "foreignField": "ressource_id",
        "as": "ressource"
    }},
    {"$unwind": "$ressource"},
    {"$lookup": {
        "from": "type",
        "localField": "properties.type_ids",
        "foreignField": "type_id",
        "as": "type"
    }}
]

project_champion = {
    "$project": {
        "champion_name": 1,
        "clans": {"$map": {"input": "$clan", "as": "clan", "in": {}}},
        "lane": 1,
        "range": 1,
        "ressource": 1,
        "sex": 1,
        "type": 1,
        "release": 1
    }
}
