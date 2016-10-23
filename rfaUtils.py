import logging
import os
import os.path
import time
from datetime import datetime

def getLog():
    i = datetime.now()
    fileName ="Logs/" + "Testrun_" + i.strftime('%Y%m%d_%H:%M') + ".log"
    try:
         open(fileName, 'a')
        # return fileName
    except IOError, e:
        print 'No such file or directory: %s' % e
        return -1

   # logging.basicConfig(filename=name, level=logging.DEBUG)
   # logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(funcName)s %(message)s', level = logging.DEBUG, filename = name)
   # logging.debug('This message should go to the log file')
   # logging.info('So should this')
   # logging.warning('And this, too')
    
    
     # create a file handler
   # logger = logging.getLogger()
    handler = logging.FileHandler(fileName)
   # handler.setLevel(logging.DEBUG)
   # formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
   # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
   # handler.setFormatter(formatter)
  #  logger.addHandler(handler)
   # logging.info("message")
   #logging.debug('This message should go to the log file')
   # logging.info('So should this')
   # logging.warning('And this, too')
    print handler

    #return fileName
    return handler
    


def qaprint(log, message):
   
   logger = logging.getLogger()
   handler = log 
   logger.setLevel(logging.DEBUG)
   formatter = logging.Formatter('%(levelname)-8s [%(asctime)s] %(funcName)s: %(message)s')
   handler.setFormatter(formatter)
   logger.addHandler(handler)
   #If fileName is returned as a log:
  # logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(funcName)s: %(message)s', level = logging.DEBUG, filename = log)
   logging.debug(message)
   logging.info(message)
   logging.warning(message)
   print message




#print getLog()