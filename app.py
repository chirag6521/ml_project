from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
import sys
import logging

print("Connecting to the database...")
if __name__=="__main__":
    logging.info("The execution has started")
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
print("Executing SQL query...")

''''
    try:
        #data_ingestion_config=DataIngestionConfig()
        data_ingestion=DataIngestion(error_details="Some error details")
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.error("Custom Exception")
        raise CustomException("An error occurred",str(e))
'''

class DataIngestion:
    def __init__(self, error_details=None):
        self.error_details = error_details

    def initiate_data_ingestion(self):
        # Your code for data ingestion goes here
        pass  # Placeholder, replace with actual implementation


data_ingestion = DataIngestion(error_details="Some error details")
data_ingestion.initiate_data_ingestion()

try:
    # Database connection code here
    print("Connected to the database")
except Exception as e:
    print("Failed to connect to the database:", str(e))


print("Fetching data...")
