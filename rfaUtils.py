'''
Created on Oct 19, 2016

@author: RAF-Team1
'''

import time
import os
import inspect

# Global variables for logs folder path and file handler.
path_to_logs = './logs'
logfile = None


# Initiate folder for logs and logger file in append mode if they don't exist and return a handler.
def getLog():
    if not os.path.exists(path_to_logs):
        os.mkdir(path_to_logs)

    # Create a new file for each new second program run.
    filename = "".join([path_to_logs,
                        "/",
                        "testrun_",
                        get_curr_time(),
                        ".log"])

    # Assign new file to a global logfile handler.
    global logfile
    if logfile is None:
        try:
            logfile = open(filename, "+a")
        except IOError:
            print("\n\nSomething went wrong on file creation.\n\n")
            return -1

    return logfile

# Append incoming message to the log file in logging format (timestamped).
def qaprint(log, message):
    stacktrace_info = getStacktraceInfo()
    timestamped_message = " ".join([get_curr_time(),
                                    " - ",
                                   stacktrace_info,
                                   str(message)])
    print(timestamped_message)
    log.write(timestamped_message +"\n")


# Get current time.
def get_curr_time():
    return time.strftime("%d-%m-%Y_%H:%M:%S")


# Get info about parent module and function from the stacktrace to use in logging message.
def getStacktraceInfo():
    stack_data = inspect.stack()
    parent_function_name = stack_data[2][3]
    parent_module_name = stack_data[-1][1].split("/")[-1]
    if parent_function_name == "<module>":
        parent_function_name = "main"
    else:
        parent_function_name = parent_function_name + "()"
    return parent_function_name + " from " + parent_module_name + ": "