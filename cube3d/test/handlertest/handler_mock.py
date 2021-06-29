#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:47
# @Description: ENTER DESCRIPTION HERE ...
# @Source: ENTER THE SOURCE HERE ...
#
#################################################
from cube3d.event import EventHandler

def make_handler_mock(board, logger):
    return EventHandlerMock(events = [], board = board, logger = logger)

class EventHandlerMock(EventHandler):
    QUIT = 'quit'
    OK   = 'ok'

    def __init__(self, events: list[str], board = None, logger = None):
        super().__init__(logger = logger, board = board)
        self.events = events

    def handle_events(self, events: list[str] = None) -> str:
        if events is not None:
            self.events = events
        debug = ''
        for event in self.events:
            if event == EventHandlerMock.QUIT:
                debug += 'Quit event Exit the system'
                return debug
            elif event == EventHandlerMock.OK:
                debug += 'Ok event received '

        return debug
