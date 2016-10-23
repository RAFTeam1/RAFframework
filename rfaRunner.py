from rfaUtils import getLog,qaprint

log = getLog()
if log == -1:
    print "Sorry, there is a problem with a log file"
else:
    message = "It is working, right?"
    qaprint(log, message)
