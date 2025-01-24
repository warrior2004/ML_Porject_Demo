import os
import sys
from src.Ml_project.exception import CustomException
from src.Ml_project.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pickle
import numpy as np

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

# Create a SQLAlchemy engine
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{db}')

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        # Use pandas read_sql_table to read the database
        df = pd.read_sql_table('students', engine)
        print(df.head())
        return df

    except Exception as e:
        raise CustomException
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)