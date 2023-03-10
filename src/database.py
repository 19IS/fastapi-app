import pymongo
from pymongo import MongoClient

from src.settings import (
    MONGO_INITDB_ROOT_PASSWORD,
    MONGO_INITDB_ROOT_USERNAME,
    MONGO_HOST,
    MONGO_PORT,
    MONGO_INITDB_DATABASE
)

MONGO_DB_CONNECTION_URL = f"mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@" \
                          f"{MONGO_HOST}:{MONGO_PORT}/?authMechanism=DEFAULT"

client = MongoClient(MONGO_DB_CONNECTION_URL)

db = client[MONGO_INITDB_DATABASE]

News = db['news']
News.create_index(
    keys=[('title', pymongo.ASCENDING)],
    unique=True,
)
