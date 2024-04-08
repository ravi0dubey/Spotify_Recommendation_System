from spotify.logger import logging
from spotify.exception import SpotifyException
import sys


def test_logger_and_exception():
    try:
        logging.info("Starting the test_logger_and_Exception")
        result = 3/0
        print(result)
        logging.info("Stopping the test_logger_and_Exception")
    except Exception as e:
        logging.info(str(e))
        raise SpotifyException(e,sys)



if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)