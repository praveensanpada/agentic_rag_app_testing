# === config/settings.py ===
import os
from dotenv import load_dotenv

load_dotenv()

GET_MONGO_URI = os.getenv("GET_MONGO_URI")
GET_MONGO_DB_NAME = os.getenv("GET_MONGO_DB_NAME")
POST_MONGO_URI = os.getenv("POST_MONGO_URI")
POST_MONGO_DB_NAME = os.getenv("POST_MONGO_DB_NAME")
PORT = int(os.getenv("PORT", 8000))