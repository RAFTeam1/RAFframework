'''
Created on Oct 19, 2016

@author: RAF-Team1
'''

import time
import os
import inspect


# Global variables for logs folder path and formatting.
path_to_logs, log_message_prefix, log_format = './logs/', "testrun_", ".log"

# Global file handler.
logfile = None


# Initiates logs folder and logger file in append mode if they don't exist and returns a file handler.
def getLog():
    # Create logs folder if not present.
    if not os.path.exists(path_to_logs):
        os.mkdir(path_to_logs)

    # Assign new file to a global logfile handler if not assigned yet or return already active file.
    global logfile
    if logfile is None:
        # Create path to file with new file name using current timestamp.
        filename = "".join([path_to_logs,
                            log_message_prefix,
                            get_curr_time(),
                            log_format])
        try:
            logfile = open(filename, "a")
        except IOError:
            print("\n\nCould not open file: " + filename + "\n\n")
            return -1

    return logfile


# Appends timestamped message to the log file with caller info for debug purpose.
def qaprint(log, message):
    stacktrace_info = getStacktraceInfo()
    timestamped_message = " ".join([get_curr_time(),
                                    " - ",
                                   stacktrace_info,
                                   str(message)])
    print(timestamped_message)
    log.write(timestamped_message +"\n")


# Gets current timestamp.
def get_curr_time():

    return time.strftime("%d-%m-%Y_%H:%M:%S")


# Gets info about parent module and function from the stacktrace to use in logging message.
def getStacktraceInfo():
    # Get list of stacktrace elements.
    stack_data = inspect.stack()

    # [0] - getStacktraceInfo() itself, [1] - qaprint, [2] - parent function
    parent_function_name = stack_data[2][3]
    parent_module_name = stack_data[2][1].split("/")[-1]  # Extract module name from full path.

    # Format for readability.
    if parent_function_name == "<module>":
        parent_function_name = "main"
    else:
        parent_function_name += "()"

    return parent_function_name + " from " + parent_module_name + ": "