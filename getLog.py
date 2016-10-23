
import os
import logging
import logging.handlers
import threading
import logging.config
import datetime

class GetLog():
    def __init__(self, path, log_file, content):
        self.path = path
        self.log_file = log_file
        self.content = content


    def get_log(self):
        current_time = self.time()
        try:
            if os.path.isdir(os.path.split(self.path )[0]):
                pass
            else:
                logfile = os.path.join(self.path)
                print logfile
                
            with threading.RLock():
                file_handler = logging.handlers.TimedRotatingFileHandler(
                    self.path, when='MIDNIGHT', backupCount=0)
                logging.root.addHandler(file_handler)
        except IOError:
            print "ok"

        formatter = logging.Formatter('%(asctime)s %(levelname)s [%(threadName)s]: %(message)s')
        logger = logging.getLogger(self.path)
        logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        lh = logging.FileHandler(self.path + current_time + " =>.." + self.log_file)
        lh.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        lh.setFormatter(formatter)
        logger.addHandler(lh)
        logger.addHandler(ch)
        logger.info(self.content)

    def time(self):
        current_time = datetime.datetime.now()
        return current_time.strftime('%Y-%m-%d %H:%M')

GetLog("/home/kateterekhova/Documents/LiClipse Workspace/Logs/", "new_data_today_test" + ".log", raw_input("text to log: ")).get_log()
