'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team X
'''
from rfaUtils import *
import sys

# parsing arguments
if len(sys.argv) != 2:
    sys.exit("Invalid number of arguments. rfaRunner accepts one argument")
tr_name = sys.argv[0]
arg = sys.argv[1].split("=")
if arg[0].lower() == "--testrun":
    if int(arg[1]) in range(0,10001):
        trid = arg[1]
    else:
        sys.exit("Invalid test run number. Valid is in [0-10000]") 
else:
    sys.exit("Invalid argument name. Valid argument is '--testrun'") 

test_cases = getTestCases(trid)
if test_cases == -1:
    sys.exit("Unable to read test cases from %s file" % trid)
print test_cases
env = getLocalEnv("local.properties")
if env == -1:
    sys.exit("Unable to read the %s file" % "local.properties")

log_location = env['log_dir']

# get the log file handle
log = getLog(log_location,tr_name)

# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "Me like what me see")

# close the log file if it open
if not log.closed:
    log.close()
