import os
from pathlib import Path
from datetime import datetime
import logging

LOG_FILE  = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.logs"
log_file_path = os.path.join(os.getcwd(), "logs",LOG_FILE)
os.makedirs(log_file_path)

LOG_FILE_PATH = os.path.join(log_file_path,LOG_FILE)


logging.basicConfig(
    filename= LOG_FILE_PATH,
    format= "[%(asctime)s] - %(lineno)s -%(name)s - %(levelname)s -%(message)s",
    level= logging.INFO
    
)