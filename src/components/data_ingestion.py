import os
import sys
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
import logging

logging.basicConfig(level=logging.INFO)

@dataclass
class DataIngestionConfig:
    #This is just a storage box of file names
    train_data_path: str = os.path.join('artifact', 'train.csv')#it means that train_data_path is "artificat/train.csv" ,os.path.join::It just joins folder + file safely
    test_data_path: str = os.path.join('artifact', 'test.csv')
    raw_data_path: str = os.path.join('artifact', 'raw.csv')

#checking everything is working fine or not:
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered data ingestion")

        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Dataset loaded")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train-test split started")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train & test separately
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))



# full flow of this data ingestion:

#Step 0: Program starts:  if __name__ == "__main__":👉 Means:“Start running from here”
#then obj = DataIngestion():object created and store it into variable; obj.initiate_data_ingestion() through this object we are calling the function

#inside function:logging.info("Entered data ingestion")👉 Just a print message,thn try block run 
#in this :df = pd.read_csv('notebook/data/stud.csv'),open the file and store it into dataframe
#logging.info("Dataset loaded"):log into the log file

#os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True):::it says that the file which is loaded previous,need to be saved somewhere ,so create artifact named folder and store the data into it;
# exist_ok=True,if exists then no error otherwise create it

 #df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True):::Save the copy of the  original data means raw data,saved as raw data
 #logging.info("Train-test split started") log into the log file

 # train_set, test_set = train_test_split(df, test_size=0.2, random_state=42):“I will divide data into two parts”80% → train (learning),,20% → test (checking)

## Save train & test separately
#train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
#test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True):::means that training data ko csv file me rkho and save it into the train_data_path(artificat folder/train.csv),similarly  with test data ,convert it into the csv file and store it into location of test_data_path(artifact folder/test.csv)


#logging.info("Data ingestion completed")log into the log file

#return (self.ingestion_config.train_data_path, self.ingestion_config.test_data_path):it means to return the train_data_path('artifact/train.csv')and return the test_data_path('artifact/test.csv')

#except Exception as e: raise CustomException(e, sys)::if any exception is raised then called the customException 
