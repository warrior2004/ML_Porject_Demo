from src.Ml_project.logger import logging
from src.Ml_project.exception import CustomException
from src.Ml_project.components.data_ingestion import DataIngestion
import sys


if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
