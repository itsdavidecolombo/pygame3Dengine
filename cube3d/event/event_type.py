#################################################
#
# @Author: davidecolombo
# @Date: mer, 30-06-2021, 10:40
# @Description: An event type enum for the application specific events
#
#################################################
import enum

class EventType(enum.Enum):

    DRAW_EVENT  = 'draw_event'
    OPEN_EVENT  = 'open_event'
    CLOSE_EVENT = 'close_event'
    USER_EVENT  = 'user_event'
