import os
import json 
from utils.logger import logging
from utils.exception import CustomException
import sys


def save_object(file_path, output_json):

    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'w') as file:
            json.dump(output_json, file , indent=4)
        logging.info(f"Object has been saved at {file_path}")
    except Exception as e:
        raise CustomException(e,sys)