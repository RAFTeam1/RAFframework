'''
Created on Oct 19, 2016

@author: sashaalexander
'''

import time
import os
import inspect

# Global variables for logs folder path and file handler.
path_to_logs = './logs'
logfile = None


# Initiate folder for logs and logger file in append mode if they don't exist.
def getLog():
    if not os.path.exists(path_to_logs):
        os.mkdir(path_to_logs)

    # Create a new file for each new second program run.
    formatted_current_time = time.strftime("_%d-%m-%Y_%H:%M:%S")
    filename = "".join([path_to_logs,
                        "/",
                        "testrun",
                        formatted_current_time,
                        ".log"])

    # Assigning new file to a global logfile handler.
    global logfile
    if logfile is None:
        try:
            logfile = open(filename, "+a")
        except IOError:
            print("\n\nSomething went wrong on file creation.\n\n")

    return logfile

# Appent incoming message to the log file in logging format (timestamped).
def qaprint(log, message):
    formatted_current_time = time.strftime("%d-%m-%Y, %H:%M:%S -")
    stacktrace_info = getStacktraceInfo()
    timestamped_message = " ".join([formatted_current_time,
                                   stacktrace_info,
                                   str(message)])
    print(timestamped_message)
    log.write(timestamped_message +"\n")

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