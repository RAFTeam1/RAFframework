import logging, datetime, os



class GetLog:

    GLOBAL_PATH = "\log\\"

    def __init__(self, test_run, app_name):
        self.test_run = test_run  #we get the number of test_run
        self.app_name = app_name  #we get the name of app

    def logger(self):
        formatter = logging.Formatter('%(levelname)s - %(asctime)s - Class: %(name)s - %(message)s')
        cur_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M')

        path = os.path.dirname(os.path.abspath(__file__)) + GetLog.GLOBAL_PATH
        if not os.path.isdir(path):
            os.makedirs(path)

        fh = logging.FileHandler(path + self.test_run + "_" + cur_time + ".log")  # give the log name. To-Do: dynamic name
        fh.setFormatter(formatter)

        ch = logging.StreamHandler()
        ch.setFormatter(formatter)

        # add handler to logger object
        logger = logging.getLogger(self.app_name)
        logger.setLevel(logging.INFO)

        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

    def debug_log(self, msg):
        self.logger().debug("Here's some debugging information about %s", msg)

    def info_log(self, msg):
        self.logger().info("Here's some info about %s", msg)

    def error_log(self, msg):
        self.logger().error(msg)

    def critical_log(self, msg):
        self.logger().critical(msg)