'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
'''
from datetime import datetime
import os


#def getLog():
def getLog(logDir, filename):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working directory + '/logs' to log_dir variable (platform independent)
   # log_dir = os.path.join(os.getcwd(), "logs")
    log_dir = os.path.join(os.getcwd(), logDir)


    # or --> script directory: log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (platform independent) in Append mode
        log = open(os.path.join(log_dir, filename + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. example: [Oct 25 01:52:33.000001] TC1 - Passed
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

def getLocalEnv(file_name):
    file_dict = {}
    try:
        f =  open(file_name, "r")
        if os.path.getsize(file_name) > 0:
            for line in f:
                pair = line.split("=")
                file_dict[pair[0].strip()] = pair[1].strip()
        f.close()  
        return file_dict
    except (OSError, IOError, EOFError):
        # return -1 in case of exception
        return -1

   

def getTestCases(trid):
    key_list = ['rest_URL', 'HTTP_method', 'HTTP_RC_desired', 'param_list']
    mega_dict = {}
    size = len(key_list)
    file_name =str(trid) +".txt"
    try:
        f =  open(file_name, "r")
        if os.path.getsize(file_name) > 0:
            for line in f:
                dataSet = line.split("|")
                single_dict = {}
                for i in range (size):
                    if key_list[i] == 'param_list':
                        single_dict [key_list[i]] = dataSet[i +1].strip().split(",")
                    else:
                        single_dict [key_list[i]] = dataSet[i +1].strip()

                mega_dict[int(dataSet[0].strip())] = single_dict
        f.close()  
        return mega_dict
    except (OSError, IOError, EOFError):
        # return -1 in case of exception
        return -1
    

def parseCmdArgs(args, argsQuantity):
    argsDict = {}
    argsDict ["filename"] =  args[0]
    for i in range (1, argsQuantity):
        try:
            pair = args[i].split("=")
            argsDict[pair[0].lower().strip()] = pair[1].strip()
        except (OSError, IOError, EOFError):
        # return -1 in case of exception
            return -1
    return argsDict
