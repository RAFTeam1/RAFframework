#!/usr/bin/env python
'''
Created on Oct 19, 2016
Updated on Oct 22, 2016

@author: sashaalexander
@coauthor: tacora
'''
from rfaUtils import getLog,qaprint

log = getLog()

message = "It is working, right?\n"
qaprint(log, message)

log.close()