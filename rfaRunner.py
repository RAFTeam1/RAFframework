'''
Created on Oct 19, 2016
@author: sashaalexander
@author: team X
@author: tacora
'''
import os
import sys
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases, getArgs, validateArgs

local_properties = "local.properties"

# get the arguments
arg = getArgs(sys.argv)
if arg == -1:
    sys.exit("Unable to parse arguments")

# check if valid args were given
validateArgs(arg)
runner_name = arg['runner_name']
trid = arg['--testrun']


# get local environment properties
env = getLocalEnv(local_properties)
if env == -1:
    sys.exit("Unable to read the %s file" % "local.properties")
log_location = env['log_dir']


# get the log file handle
log = getLog(log_location, runner_name)
if log == -1:
    sys.exit("Unable to create log file")
message = ("Testrun id: %s" % trid)


# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)


# get TCs properties for specified test run
test_cases = getTestCases(trid)
# if file doesn't exist, exit
if test_cases == -2:
    qaPrint(log, "Testrun file with id %s doesn't exist" % trid)
    sys.exit()
if test_cases == -1:
    qaPrint(log, "Unable to read test cases from testrun file $s" % trid)
    sys.exit()


# close the log file if it open
if not log.closed:
    log.close()
