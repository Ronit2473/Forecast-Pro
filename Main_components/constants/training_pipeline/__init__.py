import os
import json
import pandas as pd
import numpy as np
from datetime import datetime

'''COMMON TRAINING PIPELINE CONSTANTS'''

TARGET_COLUMN : str = "Sales"

PIPELINE_NAME : str = "ForecastPro"
ARTIFACT_DIR: str = "artifacts"

FILE_NAME: str = "train.csv"

TRAIN_SIZE: float = 0.8
TEST_SIZE: float = 0.2




'''DATA INGESTION CONSTANTS'''

DATA_INGESTION_DATABASE_NAME: str = "ForecastPro"

# Collections
DATA_INGESTION_TRAIN_COLLECTION: str = "train_data"
DATA_INGESTION_STORE_COLLECTION: str = "store_data"

# Paths
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_INGESTED_DIR: str = "ingested"

# Split ratio
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2