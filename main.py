from Main_components.exception.exception import ForecastProException
from Main_components.logging.logging import logger
from Main_components.entity.config_enitity import DataIngestionConfig, TrainingPipelineConfig,DataValidationConfig
from Main_components.entity.artifact_entity import DataIngestionArtifact
from Main_components.components.data_ingestion import DataIngestion
from Main_components.components.data_validation import DataValidation


import sys


if __name__=="__main__":

    
    try:
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        dataingestion=DataIngestion(data_ingestion_config=data_ingestion_config)
        logger.info("Initiate the data ingestion configuration")
        
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        
        logger.info("Data ingestion completed successfully")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(training_pipeline_config=training_pipeline_config)
        datavalidation=DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=data_validation_config)
        
        logger.info("Initiate the data ingestion validation")
        
        datavalidationartifact=datavalidation.initiate_data_validation()
        
        logger.info("Data validation completed successfully")
        
    except Exception as e:
        raise ForecastProException(e,sys)