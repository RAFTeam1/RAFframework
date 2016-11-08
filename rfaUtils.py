'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
@author: tacora
'''
import os
import sys
from datetime import datetime
#import traceback


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


def validateArgs(args_dict):
    # exit if number of arguments != 1
    if len(args_dict) != 2:
        sys.exit("Invalid number of arguments. %s accepts one argument" % args_dict["runner_name"])
    # exit if argument is incorrect
    if '--testrun' in args_dict:
        # exit if testrun number is out of given range
        if int(args_dict['--testrun']) not in range(0, 10001):
            sys.exit("Invalid test run number. Valid is in [0-10000]")
    else:
        sys.exit("Invalid argument name. Valid argument is '--testrun'")


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


def getTestCases(trid):
    """
    Builds a dictionary of parameters for each TC from the file content
    like: 01|/auth/login|post|200|username,password
    """
    keys = ["tcid", "rest_URL", "HTTP_method"
            , "HTTP_RC_desired", "param_list"]
    int_values = ["HTTP_RC_desired"]
    list_values = ["param_list"]
    testcases = dict()
    testcase_properties = dict()
    testrun_dir = os.path.join(os.getcwd())
    testrun_name = os.path.join(testrun_dir, trid) + ".txt"
    if not os.path.isfile(testrun_name):
        return -2
    try:
        # build the nested dictionary with parameters for each TC
        with open(testrun_name, "r") as testrun_handle:
            for line in testrun_handle:
                elements = line.strip().split("|")
                testcase_properties = dict(zip(keys[1:], elements[1:]))
                # convert required TC parameters to integers or lists
                for key, val in testcase_properties.items():
                    if key in int_values:
                        testcase_properties[key] = int(val)
                    if key in list_values:
                        val = val.strip().split(",")
                        testcase_properties[key] = val
                # build the nested dictionary: properties for each test case
                if int(elements[0]) not in testcases:
                    testcases[int(elements[0])] = testcase_properties
            return testcases
    except (OSError, IOError, IndexError):
        return -1
