'''
Created on Oct 19, 2016

@author: sashaalexander
@author: team 1
'''

from rfaUtils import getLog, qaPrint, getLocalEnv, validate_and_get_arg, getTestCases, setupLog

import sys


properties_file = "local.properties"


# Read local properties from file.
local_properties = getLocalEnv(properties_file)

if local_properties == -1:
    sys.exit("Exiting: Wasn't able to read local properties, can't proceed.")


# Setup and get log handler - one log file for the whole application.
# setupLog() uses log_dir property, stored in rfaRunner module only, to create log folder and global logger instance.
# To use a global log instance in any module use old simple getLog() without any parameters.
setupLog(local_properties["log_dir"])  # Checks are done in the method itself for better messaging.
log = getLog()
qaPrint(log, "Logger is created.")


qaPrint(log, "Running application with config parameters: " + str(local_properties))


# Usage example.
def usage():
    qaPrint(log, "Invalid parameters. Proper usage: 'rfaRunner.py --testrun=[0-10000]'")


# Process command line arguments.
qaPrint(log, "Parsing input command line arguments:")
trid = validate_and_get_arg()

if not isinstance(trid, int):
    qaPrint(log, trid)
    usage()
    sys.exit("Incorrect command line argument(s)")

# Start processing test cases.
qaPrint(log, "Running test cases " + str(trid) + ".txt according to command line argument.")


# Get test cases as a dictionary.
test_cases = getTestCases(trid)

if test_cases == -1:
    sys.exit("Could'n read test cases for id " + str(trid))


# Close the log file if it open.
if not log.closed:
    log.close()

