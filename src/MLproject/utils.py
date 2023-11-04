import os
import sys
from src.MLproject.logger import logging
from src.MLproject.exception import CustomException
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()


host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")





def get_sql_data():
    logging.info("Establishing connection with data base")
    try:
        mydb = pymysql.connect(
            host=host,
            user= user,
            password= password,
            db= db
        )

        logging.info("connection established", mydb)

        df = pd.read_sql_query("select * from student",mydb)


        return df


    except Exception as e:
        raise CustomException(e,sys)