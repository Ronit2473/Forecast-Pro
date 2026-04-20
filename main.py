from Main_components.exception.exception import ForecastProException
from Main_components.logging import logging
from Main_components.entity.config_enitity import DataIngestionConfig, TrainingPipelineConfig
from Main_components.entity.artifact_entity import DataIngestionArtifact
from Main_components.components.data_ingestion import DataIngestion

import sys


if __name__=="__main__":

    
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        dataingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.logging.info("Initiate the data ingestion configuration")
        
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        
        print(dataingestionartifact)
        
    except Exception as e:
        raise ForecastProException(e,sys)