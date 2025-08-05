# === controllers/mongo_controller.py ===
from models.mongo_model import MongoModel

mongo = MongoModel()

def get_venue_by_uid(venue_uid: str):
    return mongo.get_venue_by_uid(venue_uid)

def insert_venue_data(payload: dict):
    return mongo.insert_venue(payload)