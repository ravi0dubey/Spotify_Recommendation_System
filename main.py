from spotify.logger import logging
from spotify.exception import SpotifyException
from spotify.data_access.read_data import SpotifyData
from spotify.constant.database import COLLECTION_NAME,DATABASE_NAME
import sys,os
from pandas import DataFrame


# def test_logger_and_exception():
#     try:
#         logging.info("Starting the test_logger_and_Exception")
#         result = 3/0
#         print(result)
#         logging.info("Stopping the test_logger_and_Exception")
#     except Exception as e:
#         logging.info(str(e))
#         raise SpotifyException(e,sys)

def export_data_into_feature_store() -> DataFrame:
        """
        Export Mongodb collection record as dataframe into feature store
        get the collection name, feature store file path from data_ingestion_config
        we do not need database name as we have already declared in constant -> database.py
        """       
        try:
            logging.info("Exporting data from mongodb to feature store")
            spotify_data = SpotifyData()
            dataframe = spotify_data.export_collection_as_dataframe(COLLECTION_NAME,DATABASE_NAME)
            logging.info("Ending the export of data from mongodb to feature store")
            print(dataframe.head(5))
        except Exception as e:
            logging.info(str(e))
            raise SpotifyException(e,sys)

if __name__ == "__main__":
    try:
        export_data_into_feature_store()
        # test_logger_and_exception()
    except Exception as e:
        print(e)