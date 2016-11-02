'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
'''
from datetime import datetime
import os
import sys
import traceback


def getLog(location,filename):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working dir + '/logs' to log_dir var (OS independent)
    log_dir = os.path.join(os.getcwd(), location)
    name = filename.split(".")
    tr_name = name[0]
    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (OS independ.) in Append mode
        log = open(os.path.join(log_dir, tr_name + "_" \
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


def getLocalEnv(env_file):
    #check if file exists
    envfile_dir = os.path.join(os.getcwd())
    envfile_name = os.path.join(envfile_dir, env_file)
    properties = dict()
    if not os.path.isfile(envfile_name):
        sys.exit("%s file doesn't exist" % envfile_name)
    else:
        with open(envfile_name, "r") as env_file:
            for line in env_file:
                try:
                    line = line.split("=")
                    properties[line[0].strip()] = line[1].strip()
                except (OSError, IOError):
                    return -1
    
    return properties            
                


def getTestCases(trid):
    keys = ["tcid", "rest_URL", "HTTP_method", "HTTP_RC_desired", "param_list"]
    testrun_properties = dict()
    # if file doesn't exist, exit
    testrun_dir = os.path.join(os.getcwd())
    testrun_name = os.path.join(testrun_dir, trid) + ".txt"
    if not os.path.isfile(testrun_name):
        sys.exit("%s file doesn't exist" % testrun_name)
    else:
        try:
            with open(testrun_name, "r") as testrun_handle:
                for line in testrun_handle:
                    elements = line.split("|")
                    print elements
                    #testrun_properties = dict(zip(keys, elements))
            return testrun_properties
        except (OSError, IOError):
            return -1 

        


    