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
arg = sys.argv[1].split("=")
if arg[0].lower() == "--testrun":
    if 0 <= int(arg[1]) <= 10000:
        trid = arg[1]
    else:
        sys.exit("Invalid test run number. Valid is in [0-10000]") 
else:
    sys.exit("Invalid argument name. Valid argument is '--testrun'") 

test_cases = getTestCases(trid)
if test_cases == -1:
    sys.exit("Unable to read test cases from testrun file")


# get the log file handle
log = getLog(trid)

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
