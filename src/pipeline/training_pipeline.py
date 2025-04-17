import os ,sys
from src.logger import logging 
from src.exception import CustomException
from src.component.data_ingestion import DataIngestion
from src.component.data_transformation import DataTransformation
from src.component.model_trainer import MOdelTrainer
from dataclasses import dataclass

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.inititate_data_ingestion()
    data_tranformation = DataTransformation()
    train_arr, test_arr, _ = data_tranformation.inititate_data_transformation(train_data_path, test_data_path)
    model_training = MOdelTrainer()  # instantiate the class
    model_training.inititate_model_trainer(train_arr, test_arr) 
    
    # src\pipeline\training_pipeline.py