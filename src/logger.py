import logging #Use Python’s logging system (to save messages)
import os #Work with folders/files
from datetime import datetime #Get current time

Log_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ##Creates file name in this format like:03_22_2026_14_30_10.log::and also👉 : every run → new log file created .

logs_path=os.path.join(os.getcwd(),"logs",Log_FILE) #Create path of folder with the name of "logs" and file name is Log_FILE,which is :project/logs/03_22_2026_14_30_10.log (go to project folder-->logs folder -->then file 03_22_2026_14_30_10)
os.makedirs(logs_path,exist_ok=True) 
# exist_ok=True → no error if folder already exists,Create folder if not exists using path :logs_path

LOG_FILE_PATH=os.path.join(logs_path,Log_FILE)#👉 Full path where logs will be stored

logging.basicConfig(
  filename=LOG_FILE_PATH,
  format="[ %(asctime)s] %(lineno)d %(name)s -%(levelname)s-%(message)s",
  level=logging.INFO
)#save logs in the filename :LOG_FILE_PATH,with format,[time] line_number file_name -level-message with level is equalto info

# this is for checking purpose to  validate that logger  are working perfectly or not :
if __name__=="__main__":
  logging.info("Logging has started")