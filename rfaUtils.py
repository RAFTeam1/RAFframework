#!/usr/bin/env python
'''
Created on Oct 19, 2016
Updated on Oct 23, 2016

@author: sashaalexander
@author: tacora
'''
from os import path
import time
import datetime
import traceback

LOGPATH = "./"
TRUN_NAME = "rfaRunner"

def getlog():
    """ creates a log file and returns file handler
    """
    try:
        date_time = curr_date_time()
        logname = "_".join([TRUN_NAME, date_time]) + ".log"
        log_full_name = path.join(LOGPATH, logname)
        logfile = open(log_full_name, "a")
    except:
        traceback.print_exc()
        return -1
    return logfile
        
def qaprint(logfile, in_msg):
    """ prints message and writs message to the log file
    """
    date_time = curr_date_time(sec=True)
    log_msg = " : ".join([date_time, in_msg])
    logfile.write(log_msg)
    print log_msg

def curr_date_time(sec=None):
    """ returns timestamp in readable format
    """
    timestmp = time.time()
    if sec is True:
        date_time = datetime.datetime.fromtimestamp(timestmp).\
        strftime('%Y-%m-%d_%H:%M:%S')
    else:
        date_time = datetime.datetime.fromtimestamp(timestmp).\
        strftime('%Y%m%d_%H:%M')
    return date_time
    