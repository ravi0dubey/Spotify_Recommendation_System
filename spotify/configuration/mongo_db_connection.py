import pymongo
import sys
from spotify.exception import SpotifyException
from spotify.logger import logging
from spotify.constant.database import DATABASE_NAME
from spotify.constant.env_variable import MONGODB_URL_KEY
import certifi
ca = certifi.where()
import os

class MongoDBClient:
    client = None
    def __init__(self, database_name=DATABASE_NAME) -> None:
        try:
            if MongoDBClient.client is None:
                mongo_db_url = os.getenv(MONGODB_URL_KEY) 
                MongoDBClient.client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
            self.client = MongoDBClient.client
            self.database = self.client[database_name]
            self.database_name = database_name
        except Exception as e:
            raise SpotifyException(e,sys)