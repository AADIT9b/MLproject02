import sys
from src.logger import logging

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info() #Gets error info (line number,name,... etc.)
    file_name = exc_tb.tb_frame.f_code.co_filename
    #Gets file name where error is created

    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )#Create nice error message

    return error_message

#Create your own error type
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail)#Store detailed message in variable error_message

    def __str__(self):#👉 When printing → show custom message
        return self.error_message

# this is for checking purpose to  validate that exception  are working perfectly or not :
if __name__ == "__main__":
    try:
        a = 1 / 0   # force error
    except Exception as e:
        logging.info("Divide by 0")
        raise CustomException(e, sys)
    
#FLOW (STEP BY STEP)
#Step 1: Error happens-->a = 1 / 0-👉 Python creates error ❌
#👉 Step 2: try-except catches it,
# except Exception as e:👉 Error stored in e
#Step 3: Call your custom exception,raise CustomException(e, sys),👉 Your class is triggered 🚀

#step 4: Inside CustomException:__init__(),,👉 It calls:error_message_details(e, sys)
#👉 Step 5: Get error details::Inside function:👉 Gets:file name 📄,line number 🔢,actual error 💥
#Step 6: Create clean message::Error in file X at line Y → reason Z
#Step 7: Return message👉 Goes back to class
#Step 8: Print error__str__()👉 Shows your custom message instead of normal error