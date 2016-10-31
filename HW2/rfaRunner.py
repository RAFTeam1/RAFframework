'''
Created on Oct 19, 2016


@author: sashaalexander
@author: team X
'''
from rfaUtils import getLog, qaPrint, getLocalEnv, getTestCases

import sys

fileToDict = getLocalEnv('local.properties')
if fileToDict  == -1:
    print "Can't create a dictionary: the file is empty or doesn't exist"
else:
    # get the log file handle
    log = getLog(fileToDict['log_dir'])
    #-------------------------------------------------
# get the log file handle
#log = getLog()
#===============================
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


    
    
myDict = getTestCases(42)
if myDict  == -1:
    print "Can't create a dictionary: the file is empty or doesn't exist"
else:
    print myDict
    
