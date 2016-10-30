'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team X
'''

from datetime import datetime
import os
import sys

log_instance = None

# Setups log folder and a handler for the log file using log_dir property from config file.
def setupLog(log_dir):
    try:
        # if logs directory doesn't exist, create it.
        if not os.path.isdir(log_dir):
            os.makedirs(log_dir)
        # open log file with prefix and timestamp in Append mode, save it to log instance for all future uses.
        global log_instance
        if log_instance is None:
            filename = get_filename(log_dir)
            log_instance = open(filename, "a")
    except (OSError, IOError):
        sys.exit("Can't create logger: " + filename)  # Moved the check here for better messaging

# Returns pre-setup log instance if present or exiting with error
def getLog():
    if log_instance is None:
        sys.exit("Error. To use logger, set it up first in rfaRunner using log_dir property from config file.")
    return log_instance

# Prints timestamped message to console and saves it to the passed log file.
def qaPrint(log, message):
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    print(log_message)
    log.write(log_message + "\n")


# Returns current timestamp according to data_time_format.
def getCurTime(date_time_format):
    date_time = datetime.now().strftime(date_time_format)
    return date_time


# Constructs and returns full path to log file using sys argv.
def get_filename(log_dir):
    path_to_app_folder = "/".join(sys.argv[0].split("/")[0:-1])  # Path to application folder
    file_name = sys.argv[0].split("/")[-1]  # rfaRunner.py
    file_name = os.path.join(path_to_app_folder,
                             log_dir,
                             file_name + ": " + getCurTime("%Y%m%d_%H-%M") + ".log")
    return file_name


# Reads local properties config file and stores configs as a dictionary.
def getLocalEnv(properties_file):
    properties_dict = {}
    try:
        with open(properties_file) as file:
            data = file.read().split()
            for line in data:
                key, value = line.split("=")
                properties_dict[key] = value
    except IOError:
        return -1

    return properties_dict


# Validates command line arguments and returns test run id if valid.
def validate_and_get_arg():
    arguments = sys.argv

    if len(arguments) != 2:
        return "Error. No or too many arguments: should be 1, was " + str(len(arguments) - 1)

    first_arg = arguments[1].lower()
    if "--testrun=" not in first_arg:
        return "Error. Argument should be named 'testrun', but was " + first_arg

    first_arg_values = first_arg.split("=")
    try:
        trid = int(first_arg_values[1])
        if trid < 0 or trid > 10000:
            return "Error. Input argument should be between 0 and 10000, but was " + str(trid)
    except:
        return "Error. No integer input argument present. Argument used: " + first_arg_values[1]

    return trid


# Parses file with test cases and saves test cases to the dictionary.
def getTestCases(test_run_id):
    parameter_names = ["tcid",
                            "rest_URL",
                            "HTTP_method",
                            "HTTP_RC_desired",
                            "param_list"]
    log = getLog()
    qaPrint(log, "Parsing test cases from " + str(test_run_id) + ".txt:")
    result = {}

    try:
        with open("./" + str(test_run_id) + ".txt", "r") as file:
            data = file.read().split()

            for line in data:
                test_case_params = line.split("|")

                if len(test_case_params) != 5:
                    qaPrint(log, "List of parameters for a test case is not full")
                    return -1

                subdict = {parameter_names[1]:test_case_params[1],
                           parameter_names[2]:test_case_params[2],
                           parameter_names[3]:test_case_params[3],
                           parameter_names[4]:test_case_params[4].split(",")}
                qaPrint(log, "Test case " + test_case_params[0] + " has parameters: " + str(subdict))
                result[test_case_params[0]] = subdict
    except IOError:
        qaPrint(log, "Error while reading test cases - couldn't open file " + str(test_run_id) + ".txt")
        return -1
    
    return result
