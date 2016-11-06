'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
'''
import os
import sys
from datetime import datetime
#import traceback


def getLog(location, filename):
    """
    Creates 'logs' directory, if it doesn't exist,
    creates or opens a log file in 'logs' directory.
    """
    # assign a current working dir + '/logs' to log_dir var (OS independent)
    log_dir = os.path.join(os.getcwd(), location)
    try:
        # if logs directory(!) doesn't exist, create it
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp (OS independ.) in Append mode
        log = open(os.path.join(log_dir, filename + "_" \
                                + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError, IndexError):
        # return -1 in case of exception
        return -1


def qaPrint(log, message):
    """
    Prints 'timestamp + message' to console and writes it to the log file
    """
    # current date and time as string + message
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
    """
    Builds a dictionary of properties from envir file content
    """
    envfile_dir = os.path.join(os.getcwd())
    envfile_name = os.path.join(envfile_dir, env_file)
    properties = dict()
    #exit if test run file does not exist
    if not os.path.isfile(envfile_name):
        sys.exit("%s file doesn't exist" % envfile_name)
    else:
        try:
            # build the dictionary of properties based on file content
            with open(envfile_name, "r") as env_file:
                for line in env_file:
                    line = line.split("=")
                    properties[line[0].strip()] = line[1].strip()
            return properties
        except (OSError, IOError, IndexError):
            return -1


def getTestCases(trid):
    """
    Builds a dictionary of parameters for each TC from the file content
    """
    keys = ["tcid", "rest_URL", "HTTP_method"
            , "HTTP_RC_desired", "param_list"]
    testrun_id = dict()
    testrun_properties = dict()
    testrun_dir = os.path.join(os.getcwd())
    testrun_name = os.path.join(testrun_dir, trid) + ".txt"
    # if file doesn't exist, exit
    if not os.path.isfile(testrun_name):
        sys.exit("%s file doesn't exist" % testrun_name)
    else:
        try:
            # build the nested dictionary with parameters for each TC
            with open(testrun_name, "r") as testrun_handle:
                for line in testrun_handle:
                    elements = line.strip().split("|")
                    elements[4] = elements[4].strip().split(",")
                    elements[3] = int(elements[3])
                    testrun_properties = dict(zip(keys[1:], elements[1:]))
                    if int(elements[0]) not in testrun_id:
                        testrun_id[int(elements[0])] = testrun_properties
                return testrun_id
        except (OSError, IOError, IndexError):
            return -1


def getArgs(args):
    """
    Parses all command line arguments for runner. Returns dictionary of arguments
    """
    run_args = dict()
    try:
        # get the runner name
        args[0] = args[0].strip().split('.')
        args[0] = args[0][0]
        # add runner name to the dict
        run_args["runner_name"] = args[0]
        # build the dict from all given arguments
        for arg in args[1:]:
            arg = arg.split("=")
            run_args[arg[0].lower()] = arg[1].lower()
        return run_args
    except (OSError, IOError, IndexError):
        return -1
