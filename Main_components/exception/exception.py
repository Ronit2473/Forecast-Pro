import sys
from Main_components.logging import logging 

class ForecastProException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message=error_message
        _,_,exc_tb=error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        
        def __str__(self):
            return f"Error occured in script: {self.file_name} at line number: {self.lineno} with error message: {str(self.error_message)}"
        
        
# to check the exception handling is working or not we can run the below code snippet. It will raise an exception and we can check the log file for the error message.

'''if __name__=="__main__":

    
    try:
        logging.logging.info("Testing the exception handling")
        a=1/0
    except Exception as e:
        raise ForecastProException(e,sys)'''