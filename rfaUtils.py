'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
'''
from datetime import datetime
import os
import sys
import traceback


def getLog(filename):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working dir + '/logs' to log_dir var (OS independent)
    log_dir = os.path.join(os.getcwd(), "logs")
    # or --> script directory: 
    #log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
    # or --> user directory: 
    #log_dir = os.path.join(os.path.expanduser("~"), "logs")

    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (OS independ.) in Append mode
        log = open(os.path.join(log_dir, "rfaRunner_" \
                                + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message. 
    #example: [Oct 25 01:52:33.000001] TC1 - Passed
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    # prints log_message
    print log_message
    # writes message to a log file
    log.write(log_message + "\n")


def getCurTime(date_time_format):
    """
    Returns current date_time as a string formatted
    """
    date_time = datetime.now().strftime(date_time_format)
    return date_time

def getTestCases(trid):
    keys = ["tcid", "rest_URL", "HTTP_method", "HTTP_RC_desired", "param_list"]
    try:
        # if file doesn't exist, exit
        testrun_dir = os.path.join(os.getcwd())
        testrun_name = os.path.join(testrun_dir, trid) + ".txt"
        testrun_handle = open(testrun_name, "r")
        if not os.path.isfile(testrun_name):
            sys.exit("Testrun file doesn't exist")
        else:
            for line in testrun_handle:
                elements = line.split("|")
                testrun_properties = dict(zip(keys, elements))
            testrun_handle.close()
            return testrun_properties
        
    except (OSError, IOError):
        return -1 

    