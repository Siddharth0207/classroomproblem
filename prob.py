import json 
import pandas as pd 
import numpy as np
import os 
from utils.logger import logging
from utils.exception import CustomException
import sys
from utils.save import save_object


def load_data(file_path):
    logging.info(f"Loading data from {file_path}")
    try:
        with open(file_path, "r") as file:
            data = pd.read_csv(file)
            data = data.replace(np.nan, "NULL")
            data.columns = [col.lower().replace(" ", "_") for col in data.columns] #Creating json structured column names
            records = data.to_dict(orient="records")
            logging.info(f"data Loaded Sucessfully {len(records)} from {file_path}")
        return records
    
    except CustomException as e:
        raise CustomException(f"Error occured while loading data from {file_path} {str(e)}", sys)


# Creating json structured column names    
def structure_by_student(records):
    """
    Group records by student_id into a nested JSON structure.
    
    """
    try:
        logging.info(f"Structuring data by student")
        student_data = {}
        for record in records:
            student_id = str(record["student_id"])  # Convert to string for JSON keys
            if student_id not in student_data:
                student_data[student_id] = []
            student_data[student_id].append(record)
        return student_data
    except CustomException as e:
        raise CustomException(f"Error occured while structuring data by student {str(e)}", sys)


def save_json(data, output_file):
    logging.info(f"saving json file initiated")
    try:
        save_object(output_file, data)
        logging.info(f"Data saved to {output_file}")
        logging.info(f"data saved succesfully")
    except CustomException as e:
        raise CustomException(f"Error occured while saving data to {output_file} {str(e)}", sys)