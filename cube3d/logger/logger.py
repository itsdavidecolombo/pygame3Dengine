#################################################
#
# @Author: davidecolombo
# @Date: mar, 29-06-2021, 10:17
# @Description: The Logger class for logging debug, warning and error allover the application
#
#################################################
from cube3d.logger import LoggerLevel

class Logger:

    def __init__(self, guard = None):
        self.guard = guard

    def set_guard(self, guard):
        if self.guard is not None:
            raise ValueError('Logger: guard is not None...')
        self.__safe_init_guard(guard)

    def __safe_init_guard(self, guard):
        if guard is None:
            raise ValueError('Logger: guard is None...')
        self.guard = guard

    def log(self, level: LoggerLevel, msg: str = ''):
        header = f'[{level}]\t'
        if level == LoggerLevel.Severe:
            print(header + msg)
            self.guard.safe_shut_down()
        print(header + msg)
