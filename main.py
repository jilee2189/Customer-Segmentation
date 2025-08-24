from customer_personas.components.data_ingestion import DataIngestion
from customer_personas.exception.exception import CustomerException
from customer_personas.logging.logger import logging
from customer_personas.entity.config_entity import DataIngestionConfig
from customer_personas.entity.config_entity import TrainingPipelineConfig


if __name__=='__main__':
    try: 
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiated the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data Initiation Completed")
        print(dataingestionartifact)
    except Exception as e: 
        raise CustomerException(e, sys)

