from datetime import datetime
import os
from cgi import log

def getLog():
    """
    1. Creates 'logs' directory, if it doesn't exist,
    2. Creates or opens a log file in 'logs' directory.
    """
    log_dir = os.path.join(os.getcwd(), "logs")
    try:
        # if logs directory doesnt exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in append mode
        log = open(os.path.join(log_dir, "rfaRunner_" + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1
    
def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string  + message . Example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")
           


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted according to date_time_format
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time