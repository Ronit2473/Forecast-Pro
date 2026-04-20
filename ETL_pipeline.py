import os 
import sys
import json

from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URI")

print(MONGO_DB_URL)

import certifi
ca=certifi.where()


import pymongo
import numpy as np
import pandas as pd

from Main_components.exception.exception import ForecastProException
from Main_components.logging.logging import logging

class Extact_data:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise ForecastProException(e,sys)
    
    def csv_to_json_convertor(self,file_path):
        try:
            data=pd.read_csv(file_path)
            data.reset_index(inplace=True,drop=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise ForecastProException(e,sys)
        
        
    def insert_data_to_mongodb(self,records,database,collection):
        try:
            self.database=database
            self.collection=collection
            self.records=records
                
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            self.database=self.mongo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise ForecastProException(e,sys)
            

if __name__=="__main__":
    forecastobj = Extact_data()
    #for train dataset
    FILE_PATH_1 = r"E:\forecast_pro\Dataset\train.csv"
    database = "ForecastPro"
    collection_1 = "train_data"

    records_1 = forecastobj.csv_to_json_convertor(file_path=FILE_PATH_1)

    no_of_records_1 = forecastobj.insert_data_to_mongodb(
        records=records_1,
        database=database,
        collection=collection_1
    )

    print("Train records inserted:", no_of_records_1)
    
    #for store dataset
    FILE_PATH_2 = r"E:\forecast_pro\Dataset\store.csv"
    collection_2 = "store_data"
    records_2 = forecastobj.csv_to_json_convertor(file_path=FILE_PATH_2)

    no_of_records_2 = forecastobj.insert_data_to_mongodb(
        records=records_2,
        database=database,
        collection=collection_2
    )

    print("Store records inserted:", no_of_records_2)
    
    
        