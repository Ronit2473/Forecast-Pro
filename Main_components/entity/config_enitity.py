from datetime import datetime

import os

from Main_components.constants import training_pipeline


print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)


class TrainingPipelineConfig:
    def __init__(self,timestamp=datetime.now()):
        timestamp = timestamp.strftime("%m-%d-%Y-%H-%M-%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,timestamp)
        self.timestamp:str=timestamp
        

import os

class DataIngestionConfig:

    def __init__(
        self,
        training_pipeline_config: TrainingPipelineConfig
    ):

        # Root ingestion directory
        self.data_ingestion_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_INGESTION_DIR_NAME
        )

        # Feature store path
        self.feature_store_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,
            "train.csv"
        )

        # Train file path
        self.training_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            "train.csv"
        )

        # Test file path
        self.test_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            "test.csv"
        )

        # NEW — Store file path
        self.store_file_path: str = os.path.join(
            self.data_ingestion_dir,
            training_pipeline.DATA_INGESTION_INGESTED_DIR,
            "store.csv"
        )

        # Split ratio
        self.train_test_split_ratio: float = (
            training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        )

        # Train collection
        self.collection_name: str = (
            training_pipeline.DATA_INGESTION_TRAIN_COLLECTION
        )

        # NEW — Store collection
        self.store_collection_name: str = (
            training_pipeline.DATA_INGESTION_STORE_COLLECTION
        )

        # Database name
        self.database_name: str = (
            training_pipeline.DATA_INGESTION_DATABASE_NAME
        )
        
        
class DataValidationConfig:
    def __init__(self, training_pipeline_config: TrainingPipelineConfig):
        self.data_validation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_VALIDATION_DIR_NAME
        )
        
        self.valid_data_dir: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_VALID_DIR
        )
        
        self.invalid_data_dir: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_INVALID_DIR
        )
        
        self.valid_train_file_path: str = os.path.join(
            self.valid_data_dir,
            training_pipeline.FILE_NAME
        )
        
        self.valid_test_file_path: str = os.path.join(
            self.valid_data_dir,
            training_pipeline.FILE_NAME
        )
        
        self.invalid_train_file_path: str = os.path.join(
            self.invalid_data_dir,
            training_pipeline.FILE_NAME
        )
        
        self.invalid_test_file_path: str = os.path.join(
            self.invalid_data_dir,
            training_pipeline.FILE_NAME
        )
        
        
        self.drift_report_file_path: str = os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )
        
