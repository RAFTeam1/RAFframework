import time

from rfaUtils import getLog, qaprint


def testLoggerOutsideRunner():
    # Wait for specified amount of seconds.
    time.sleep(5)
    logger = getLog()
    qaprint(logger, "Appends to the same file after a long sleep!")
    time.sleep(15)
    qaprint(logger, "Will be one file for the whole program run")