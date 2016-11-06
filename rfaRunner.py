'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team X
'''
import sys
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases, getArgs

# get the arguments
arg = getArgs(sys.argv)
if arg == -1:
    sys.exit("Unable to parse arguments")
# exit if number of arguments != 1
if len(arg) != 2:
        sys.exit("Invalid number of arguments. rfaRunner accepts one argument")
tr_name = arg['runner_name']
# exit if argument is incorrect
if '--testrun' in arg:
    # exit if testrun number is out of given range
    if int(arg['--testrun']) in range(0, 10001):
        trid = arg['--testrun']
    else:
        sys.exit("Invalid test run number. Valid is in [0-10000]")
else:
    sys.exit("Invalid argument name. Valid argument is '--testrun'")


# get TCs properties for specified test run
test_cases = getTestCases(trid)
# exit if getting TCs' properties failed
if test_cases == -1:
    sys.exit("Unable to read test cases from %s file" % trid)
print test_cases
# get local environment properties
env = getLocalEnv("local.properties")
# exit if reading envir properties failed
if env == -1:
    sys.exit("Unable to read the %s file" % "local.properties")
log_location = env['log_dir']

# get the log file handle
log = getLog(log_location, tr_name)
# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
#qaPrint(log, "Me like what me see")

# close the log file if it open
if not log.closed:
    log.close()
