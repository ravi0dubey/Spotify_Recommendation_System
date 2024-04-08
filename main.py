from spotify.logger import logging
from spotify.exception import SpotifyException
import sys


def test_logger_and_exception():
    try:
        result = 3/0
        print(result)
    except Exception as e:
        raise SpotifyException(e,sys)



if __name__ == "__main__":
    try:
        test_logger_and_exception()
    except Exception as e:
        print(e)