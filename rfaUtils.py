#!/usr/bin/env python
'''
Created on Oct 19, 2016
Updated on Oct 22, 2016

@author: sashaalexander
@coauthor: tacora
'''
from os import path
import time
import datetime
#import traceback
logpath = "/home/korvin/RAF/RAF_CODE/"
trun_name = "rfaRunner"

def getLog():
    try:
        date_time = curr_date_time()
        logname = "_".join([trun_name, date_time]) + ".log"
        log_full_name = path.join(logpath, logname)
        logfile = open(log_full_name, "a")
        return logfile
    except:
        #traceback.print_exc()
        return -1

def qaprint(logfile, in_msg):
    date_time = curr_date_time(sec=True)
    log_msg = " : ".join([date_time, in_msg])
    logfile.write(log_msg)
    print log_msg  

def curr_date_time(sec=None):
    timestmp = time.time()
    if sec is True:
        date_time = datetime.datetime.fromtimestamp(timestmp).strftime('%Y%m%d_%H:%M:%S')
    else:
        date_time = datetime.datetime.fromtimestamp(timestmp).strftime('%Y%m%d_%H:%M')
    return date_time
    