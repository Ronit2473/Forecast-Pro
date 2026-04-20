import yaml
import pickle
#import dill
import os,sys
import numpy as np
from Main_components.exception.exception import ForecastProException
from Main_components.logging.logging import logger


def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise ForecastProException(e,sys) from e