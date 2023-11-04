from src.MLproject.components.data_ingestion import DataIngestionConfig,DataIngestion
from src.MLproject.logger import logging
from src.MLproject.exception import CustomException
import sys




if __name__ =="__main__":


    try:
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion_config()
    except Exception as e:
        raise CustomException (e,sys)