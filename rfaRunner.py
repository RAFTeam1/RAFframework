'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team X
'''
#Start from command line with   sudo python rfaRunner.py --testrun=42

from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases, parseCmdArgs

import sys
argsQuantity = len(sys.argv)

# ---------------------------------

if argsQuantity < 2:
    sys.exit("Incorrect request was entered, example of correct one: rfaRunner.py --testrun=42")

argsDict = parseCmdArgs(sys.argv, argsQuantity)
if argsDict == -1:
    sys.exit("Incorrect set of arguments was entered, example of correct one: rfaRunner.py --testrun=42")

trid = int(argsDict["--testrun"])


fileToDict = getLocalEnv('local.properties')
if fileToDict  == -1:
    sys.exit("Can't create a dictionary: the file local.properties is empty or doesn't exist")
else:
    # get the log file handle
    log = getLog(fileToDict['log_dir'], argsDict ["filename"] )

#===============================
# exit if log creation failed
if log == -1:
    sys.exit("Unable to create log file")

message = "It is working, right?"

# call qaPrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
#qaPrint(log, "Me like what me see")


    
myDict = getTestCases(trid)
if myDict  == -1:
    qaPrint(log, "Can't create a dictionary: the file is empty or doesn't exist")
    
# close the log file if it open
if not log.closed:
    log.close()


    
