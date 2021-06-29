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

    def __init__(self, guard):
        super().__init__(guard)

    def log(self, level: LoggerLevel, msg: str = '') -> str:
        if level == LoggerLevel.Severe:
            return self.guard.safe_shut_down()
        return msg
