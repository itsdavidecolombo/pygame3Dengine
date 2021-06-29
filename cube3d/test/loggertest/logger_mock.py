#################################################
#
# @Author: davidecolombo
# @Date: mar, 29-06-2021, 10:32
# @Description: Logger mock class for testing the logging
#
#################################################
from cube3d.logger import Logger, LoggerLevel

def make_logger_mock(guard):
    return LoggerMock(guard)

class LoggerMock(Logger):

    def __init__(self, guard = None):
        super().__init__(guard)

    def log(self, level: LoggerLevel, msg: str = '') -> str:
        debug = ''
        if level == LoggerLevel.Severe:
            debug += 'Level Severe received Exit the system'
            return debug
        return msg
