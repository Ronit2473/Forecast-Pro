from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    train_file_path: str
    test_file_path: str
    store_file_path: str
    
    
@dataclass
class DataValidationArtifact:

    validation_status: bool

    valid_train_file_path: str
    valid_store_file_path: str

    invalid_train_file_path: str
    invalid_store_file_path: str

    drift_report_file_path: str
    