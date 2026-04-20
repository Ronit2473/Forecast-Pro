from Main_components.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataValidationArtifact
from Main_components.entity.config_enitity import DataValidationConfig
from Main_components.exception.exception import ForecastProException
from Main_components.constants.training_pipeline import SCHEMA_FILE_PATH
import sys
import os
from Main_components.logging.logging import logger
from Main_components.utils.main_utils.utils import read_yaml_file
import pandas as pd
from scipy.stats import ks_2samp

class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionArtifact,data_validation_config:DataValidationConfig):
        try:
            
            self.data_ingestion_artifact=data_ingestion_artifact
            self.data_validation_config=data_validation_config
            self.schema_config=read_yaml_file(SCHEMA_FILE_PATH)
        except Exception as e:
            raise ForecastProException(e,sys)
        
        
    
    def initiate_data_validation(self) -> DataValidationArtifact:

        try:
            logger.info("Starting data validation")

            # Load datasets

            train_df = pd.read_csv(
                self.data_ingestion_artifact.train_file_path
            )

            store_df = pd.read_csv(
                self.data_ingestion_artifact.store_file_path
            )

            # Validate TRAIN columns

            expected_train_columns = list(
                self.schema_config["train_columns"].keys()
            )

            missing_train_columns = set(
                expected_train_columns
            ) - set(train_df.columns)

            if missing_train_columns:

                raise Exception(
                    f"Missing train columns: {missing_train_columns}"
                )

            # Validate STORE columns

            expected_store_columns = list(
                self.schema_config["store_columns"].keys()
            )

            missing_store_columns = set(
                expected_store_columns
            ) - set(store_df.columns)

            if missing_store_columns:

                raise Exception(
                    f"Missing store columns: {missing_store_columns}"
                )

            logger.info("Column validation successful")

            # Create directories

            valid_dir = "artifacts/data_validation/valid"
            invalid_dir = "artifacts/data_validation/invalid"

            os.makedirs(valid_dir, exist_ok=True)
            os.makedirs(invalid_dir, exist_ok=True)

            # Paths

            valid_train_path = os.path.join(
                valid_dir,
                "train.csv"
            )

            valid_store_path = os.path.join(
                valid_dir,
                "store.csv"
            )

            invalid_train_path = os.path.join(
                invalid_dir,
                "train.csv"
            )

            invalid_store_path = os.path.join(
                invalid_dir,
                "store.csv"
            )

            # Save validated datasets

            train_df.to_csv(
                valid_train_path,
                index=False
            )

            store_df.to_csv(
                valid_store_path,
                index=False
            )

            logger.info("Datasets saved to valid folder")

            return DataValidationArtifact(

                validation_status=True,

                valid_train_file_path=valid_train_path,
                valid_store_file_path=valid_store_path,

                invalid_train_file_path=invalid_train_path,
                invalid_store_file_path=invalid_store_path,

                drift_report_file_path=
                    "artifacts/data_validation/drift_report.json"
            )

        except Exception as e:

            logger.error("Data validation failed")

            return DataValidationArtifact(

                validation_status=False,

                valid_train_file_path=None,
                valid_store_file_path=None,

                invalid_train_file_path=None,
                invalid_store_file_path=None,

                drift_report_file_path=None
            )