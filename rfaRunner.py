from rfaUtils import getLog, qaPrint
import sysconfig

# get the log file handler
log = getLog()

# exit if log creation is FAILED
if log == -1:
    sys.exit("Unable to create log file")
message = "It is working, right?"

# call qePrint to print a message with timestamp and write it to the log file
qaPrint(log, message)
qaPrint(log, "hello world")

# close the log file
if not log.closed:
    log.close()
