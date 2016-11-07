'''
Created on Oct 19, 2016
@author: sashaalexander
@author: team X
'''
import os
import sys
from datetime import datetime


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
    print(log_message)
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
    Builds a dictionary of properties from local properties file content
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
    like: 01|/auth/login|post|200|username,password
    """
    keys = ["tcid", "rest_URL", "HTTP_method",
            "HTTP_RC_desired", "param_list"]
    int_values = ["HTTP_RC_desired"]
    test_cases_dict = dict()
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
                    testrun_properties = dict(zip(keys[1:], elements[1:]))
                    # convert required TC parameters to integers
                    for key, val in testrun_properties.items():
                        if key in int_values:
                            testrun_properties[key] = int(val)
                    if int(elements[0]) not in test_cases_dict:
                        test_cases_dict[int(elements[0])] = testrun_properties
                return test_cases_dict
        except (OSError, IOError, IndexError):
            return -1


def getArgs(args):
    """
    Parses all command line arguments for runner. Returns dictionary of arguments
    """
    run_args = dict()
    try:
        # get the runner name (without .py)
        args[0] = args[0].strip().split('.')
        args[0] = args[0][0]
        # add runner name to the dict
        run_args["runner_name"] = args[0]
        # build the dict from all given arguments
        for arg in args[1:]:
            arg = arg.split("=")
            run_args[arg[0].lower()] = arg[1].lower()

        # exit if number of arguments != 1
        if len(run_args) != 2:
            sys.exit("Invalid number of arguments. rfaRunner accepts one argument")
        return run_args
    except (OSError, IOError, IndexError):
        return -1

def validate_testrun(args):
    """
    Validates testrun parameter in command line arguments.
    Returns -1 in case of any error to print usage example in rfaRunner
    """
    if '--testrun' in args:
        if int(args['--testrun']) in range(0, 10001):
            return args['--testrun']
    else:
        return -1
