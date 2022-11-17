from pymongo import MongoClient
import settings

mongodb_client = MongoClient(settings.mongodb_uri, settings.port)
mongodb_db = mongodb_client["iot"]
mongodb_collection = mongodb_db["esp8266"]
