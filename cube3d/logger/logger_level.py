#################################################
#
# @Author: davidecolombo
# @Date: mar, 29-06-2021, 10:26
# @Description: Enum for logger level
#
#################################################
import enum

class LoggerLevel(enum.Enum):
    Severe  = 10
    Warning = 8
    Info    = 4
    Debug   = 0
