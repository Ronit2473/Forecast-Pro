from Main_components.exception.exception import ForecastProException
import pymongo
from Main_components.logging.logging import logger
import os
from Main_components.entity.config_enitity import DataIngestionConfig
from Main_components.entity.artifact_entity import DataIngestionArtifact
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from dotenv import load_dotenv

load_dotenv()

MONGO_DB_URL=os.getenv("MONGO_DB_URL")


class DataIngestion:

    def __init__(self, data_ingestion_config):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ForecastProException(e, sys)


    def export_collection_as_dataframe(self,collection_name):

        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)

            collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))

            
            if "_id" in df.columns:
                df = df.drop("_id", axis=1)

            
            df.replace({'na': np.nan}, inplace=True)

            return df

        except Exception as e:
            raise ForecastProException(e, sys)


    def export_data_into_feature_store(self, dataframe: pd.DataFrame):

        try:
            feature_store_file_path = (
                self.data_ingestion_config.feature_file_store_path
            )

            dir_path = os.path.dirname(feature_store_file_path)

            os.makedirs(dir_path, exist_ok=True)

            dataframe.to_csv(
                feature_store_file_path,
                index=False,
                header=True
            )

            return dataframe

        except Exception as e:
            raise ForecastProException(e, sys)
            
            
        except Exception as e:
            raise ForecastProException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            logger.info("Starting data ingestion")

        # STEP 1 — Load TRAIN data
            train_df = self.export_collection_as_dataframe(
            collection_name="train_data"
        )

        # STEP 2 — Load STORE data
            store_df = self.export_collection_as_dataframe(
            collection_name="store_data"
        )

            logger.info("Both datasets loaded from MongoDB")

        # STEP 3 — Save to feature store

            feature_store_dir = \
                self.data_ingestion_config.feature_store_file_path

            os.makedirs(feature_store_dir, exist_ok=True)

            train_feature_path = os.path.join(
                feature_store_dir,
                "train.csv"
                )

            store_feature_path = os.path.join(
                feature_store_dir,
                "store.csv"
            )

            train_df.to_csv(train_feature_path, index=False)
            store_df.to_csv(store_feature_path, index=False)

            logger.info("Train and Store data saved to feature store")

        # STEP 4 — Create artifact

            data_ingestion_artifact = DataIngestionArtifact(
                train_file_path=
                self.data_ingestion_config.training_file_path,

                test_file_path=
                self.data_ingestion_config.test_file_path,
                
                store_file_path=
                self.data_ingestion_config.store_file_path
        )

            logger.info("Data ingestion completed")

            return data_ingestion_artifact

            
            
        except Exception as e:
            raise ForecastProException(e,sys)
