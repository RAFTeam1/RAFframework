#!/usr/bin/env python
'''
Created on Oct 19, 2016
Updated on Oct 23, 2016

@author: sashaalexander
@author: tacora
'''
from rfaUtils import getlog, qaprint

def run_getlog():
    """ calls getlog() and qaprint()
    """
    log = getlog()
    message = "It is working, right?\n"
    qaprint(log, message)

if __name__ == "__main__":
    run_getlog()