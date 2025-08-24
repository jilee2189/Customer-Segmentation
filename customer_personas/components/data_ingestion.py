from customer_personas.exception.exception import CustomerException
from customer_personas.logging.logger import logging

## configuration of the Data Ingestion Config 

from customer_personas.entity.config_entity import DataIngestionConfig
from customer_personas.entity.config_entity import TrainingPipelineConfig

import pandas as pd 
import os 
import sys 
import numpy as np 
import pymongo
from typing import List

from dotenv import load_dotenv 
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion: 
    def __init__(self, data_ingestion_config :DataIngestionConfig): 
        try: 
            self.data_ingestion_config = data_ingestion_config
        except Exception as e: 
            raise CustomerException(e, sys)
        
    def export_collection_as_dataframe(self): 
        """
        Read data from Mongodb 
        """
        try: 
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name
            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection = self.mongo_client[database_name][collection_name]
            df=pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list(): 
                df = df.drop(columns = ["_id"], axis = 1)
            df.replace({"na":np.nan}, inplace=True)
            return df 
        except Exception as e: 
            raise CustomerException    
        
    def export_data_into_feature_store(self,dataframe: pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            #creating folder
            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise CustomerException(e,sys)    
    
    def initiate_data_ingestion(self): 
        try: 
            dataframe=self.export_collection_as_dataframe() 
            dataframe=self.export_data_into_feature_store(dataframe)
            dataingestionartifact = dataframe 
            return dataingestionartifact

        except Exception as e: 
            raise CustomerException