import os 
import sys 
import json 

from dotenv import load_dotenv 
load_dotenv() 

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi 
ca = certifi.where() 

import pandas as pd 
import numpy as np 
import pymongo 
from customer_personas.exception.exception import CustomerException
from customer_personas.logging.logger import logging

class DataExtract(): 
    def __init__(self):
        try: 
            pass
        except Exception as e: 
            raise CustomerException(e, sys)
        
    def csv_to_json_converter(self, file_path): 
        try: 
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(data.to_dict(orient="records"))
            return records 
        except Exception as e: 
            raise CustomerException(e, sys)
    
    def insert_data_mongodb(self, records, database, collection): 
        try: 
            self.database = database 
            self.collection = collection 
            self.records = records 
            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        except Exception as e: 
            raise CustomerException(e, sys)

if __name__== '__main__': 
    FILE_PATH = r'C:\Users\19258\Desktop\customer personality analysis kaggle\marketing_campaign.csv'
    DATABASE = "jilee2189"
    Collection = "customer_personas"
    networkobj = DataExtract()
    records = networkobj.csv_to_json_converter(file_path=FILE_PATH)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records, DATABASE, Collection)
    print(no_of_records)

