'''
Created on Oct 19, 2016

@author: sashaalexander
'''
from rfaUtils import getLog, qaprint

log = getLog()

message = "It is working, right?"
qaprint(log, message)


# Testing logger
def test():
    qaprint(log, "logging a lot of nums")
    for i in range(30):
        qaprint(log, i)


test()