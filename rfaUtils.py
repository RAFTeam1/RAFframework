from datetime import datetime
import os


def validate_and_get_arg():
    arguments = (raw_input("Enter test. Format example ' --testrun=42.txt ': ")).lower().split("=")

    first_arg = arguments[0].lower()
    if "--testrun" not in first_arg:
        print( "Error. Argument should be named 'testrun', but was " + first_arg)
        return -1

    first_arg_values = arguments[1].split(".txt")
    try:
        trid = int(first_arg_values[0])

        if trid < 0 or trid > 10000:
            print( "Error. Input argument should be between 0 and 10000, but was " + str(trid))
            return -1
    except:
        print("Error. No integer input argument present. Argument used: " + first_arg_values[1])
        return -1
    return str(trid)


def getLog(path, file_name):

    try:
        if not os.path.isdir(path):
            os.makedirs(path)
        log = open(os.path.join(path, file_name + "=>" + getCurTime("%Y%m%d_%H-%M") + ".log"), "a")
        return log
    except (OSError, IOError):
        return -1


def qaPrint(log, message):
    log_message = getCurTime("[%b %d %H:%M:%S.%f]") + " " + message
    print (log_message)
    log.write(log_message + "\n")


def getCurTime(date_time_format):
    date_time = datetime.now().strftime(date_time_format)
    return date_time


def getLocalEnv (local_properties):
        dict_properties = {}
        try:
            with open(local_properties) as file:
                for line in file:
                    if len(line) > 0 and "=" in line:
                        (key,val) = line.strip().split('=')
                        dict_properties[key]=val
            return dict_properties

        except (IOError):
            return -1


def getTestCases (test_run_id):
        try:
            keys_name = ["tcid", "rest_URL", "HTTP_method", "HTTP_RC_Desired", "param_list"]
            with open(test_run_id)as data:
                mega_dict = {}
                for line in data:
                    ls= line.strip().split("|")
                    key = ls[0]
                    d = {}
                    d[key] = {}
                    d[key][keys_name[1]] = ls[1]
                    d[key][keys_name[2]] = ls[2]
                    d[key][keys_name[3]] = ls[3]
                    d[key][keys_name[4]] = list(ls[4].split(','))
                    mega_dict.update(d)

                return mega_dict
        except IOError:
            return -1
