from rfaUtils import GetLog

class Runner:
    logging = GetLog("first_run","Runner")

    def def_test(self):
        try:
            a = 2/2
            message = "It is working, right?"
            Runner.logging.info_log(message)
        except:
            message = "It is not working, right?"
            Runner.logging.error_log(message)

Runner().def_test()
