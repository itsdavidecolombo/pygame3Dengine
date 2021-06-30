#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:47
# @Description: ENTER DESCRIPTION HERE ...
# @Source: ENTER THE SOURCE HERE ...
#
#################################################
from cube3d.event import EventHandler, EventType

def make_handler_mock(board, logger, window):
    return EventHandlerMock(board = board, logger = logger, window = window)

class EventHandlerMock(EventHandler):

    def __init__(self, board = None, window = None, logger = None):
        super().__init__(logger = logger, window = window, board = board)

    def handle_events(self, event: EventType) -> str:
        debug = ''
        if event == EventType.DRAW_EVENT:
            debug += 'Drawing objects'
            return debug
        elif event == EventType.OPEN_EVENT:
            debug += 'Opening the window'
            return debug
        elif event == EventType.CLOSE_EVENT:
            debug += 'Closing the window'
            return debug
        elif event == EventType.USER_EVENT:
            debug += 'User event received'
            return debug
        else:
            debug += 'Unknown event Exit the system'
            return debug
