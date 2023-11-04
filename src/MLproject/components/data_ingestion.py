import os
import sys
import pandas as pd
from src.MLproject.logger import logging
from src.MLproject.exception import CustomException
from dataclasses import dataclass
from src.MLproject.utils import get_sql_data
from sklearn.model_selection import train_test_split


@dataclass
class DataIngestionConfig:
    train_data_path = os.path.join("artifacts", "train.csv")
    test_data_path = os.path.join("artifacts","test.csv")
    raw_data_path = os.path.join("artifacts","raw.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initiate_data_ingestion_config(self):
        try:

            df = get_sql_data()

            logging.info("reading daat from mysql is completed")
            

            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False, header= True)

            train_data, test_data = train_test_split(df, test_size=0.2, random_state=42)

            train_data.to_csv(self.ingestion_config.train_data_path,index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False, header=True)


            logging.info("Reading data mysql is completed")


            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
                  


        except Exception as e:
            raise CustomException(e,sys)