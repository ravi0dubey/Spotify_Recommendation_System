import logging
import os
from datetime import datetime

LOG_FILE_NAME = f"{datetime.now().strftime('%m%d%Y_%H%M%S')}.log"
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")
# print("inside logger:" + f"{LOG_FILE_DIR}")
# print("inside logger:" + f"{LOG_FILE_NAME}")

# create log file folder if it does not exists
os.makedirs(LOG_FILE_DIR,exist_ok= True)

# log file
LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s]%(lineno)d %(name)s - %(levelname)s - %(message)s", 
    level= logging.DEBUG,

)



