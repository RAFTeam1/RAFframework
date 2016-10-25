'''
Created on Oct 19, 2016

@author: sashaalexander
'''
import subRunner

from rfaUtils import getLog, qaprint


log = getLog()

message = "It is working, right?"
qaprint(log, message)


# Tests how would logger behave if called repeatedly
def testLoggerInsideRunner():
    qaprint(log, "logging a lot of nums")
    for i in range(10):
        qaprint(log, i)


testLoggerInsideRunner()

# Tests how logger would be called from another module in different time
subRunner.testLoggerOutsideRunner()