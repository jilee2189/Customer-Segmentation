import os
import sys 
import numpy as np 
import pandas as pd

"""
defining common constant variable for training pipeline
"""
TARGET_COLUMN = "Response"
PIPELINE_NAME: str = "customer_personas"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "marketing_campaign.csv"


SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")

SAVED_MODEL_DIR =os.path.join("saved_models")
MODEL_FILE_NAME = "model.pkl"




"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "customer_personas"
DATA_INGESTION_DATABASE_NAME: str = "jilee2189"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
