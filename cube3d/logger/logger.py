#################################################
#
# @Author: davidecolombo
# @Date: mar, 29-06-2021, 10:17
# @Description: The Logger class for logging debug, warning and error allover the application
#
#################################################
from cube3d.logger import LoggerLevel

class Logger:

    def __init__(self, guard):
        self.guard = guard

    def log(self, level: LoggerLevel, msg: str = '') -> bool:
        if level == LoggerLevel.Severe:
            self.guard.safe_shut_down()
            return False
        print(msg)
        return True
