'''
Created on Nov 7, 2016
@author: sashaalexander
@author: team 1
'''

import sys
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases, getArgs, validate_testrun


local_properties = "local.properties"

# get and save command line arguments to the args dictionary
args = getArgs(sys.argv)
if args == -1:
    sys.exit("Unable to parse arguments")

# get local environment properties
env = getLocalEnv(local_properties)
if env == -1:
    sys.exit("Unable to read the %s file" % "local.properties")

# get the log file handle
application_name = args['runner_name']
log_location = env['log_dir']

log = getLog(log_location, application_name)
if log == -1:
    sys.exit("Unable to create log file")

# start logging
qaPrint(log, "Logger is created. Running application with config parameters: \n " + str(env))


# get and validate test run id from the command line parameter in args dictionary
def usage():
    qaPrint(log, "Invalid parameters. Proper usage: 'rfaRunner.py --testrun=[0-10000]'")

trid = validate_testrun(args)
if trid == -1:
    usage()
    sys.exit("Incorrect or missing testrun argument")


# get TCs properties for specified test run
qaPrint(log, "Reading test cases from " + str(trid) + ".txt according to testrun argument.")

test_cases = getTestCases(trid)
if test_cases == -1:
    qaPrint(log, "Unable to read test cases from %s file" % trid)
    sys.exit("Unable to read test cases from %s file" % trid)

qaPrint(log, "Test cases: \n %s" % test_cases)


#old message to test the logger - can be deleted now
message = "It is working, right?"
qaPrint(log, message)

# close the log file if it open
if not log.closed:
    log.close()
