from src.MLproject.logger import logging
import sys



def get_error_detail(error, error_detail:sys):

    """
    Args: error, error detail which will be sys format
    """
    _,_,exc_tb = error_detail.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error in occured in python script [{0}] in line no [{1}] and message is [{2}]".format(
        filename, exc_tb.tb_lineno, str(error)        
    )

    return error_message




class CustomException(Exception):
    def __init__(self, error_message, error_details:sys) -> None:
        super().__init__(self, error_message)
        self.error_message = get_error_detail(error_message,error_details)


    def __str__(self):
        return self.error_message

