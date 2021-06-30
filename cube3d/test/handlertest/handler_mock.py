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
    return EventHandlerMock(events = [], board = board, logger = logger, window = window)

class EventHandlerMock(EventHandler):
    QUIT = 'quit'
    OK   = 'ok'

    def __init__(self, events: list[str], board = None, window = None, logger = None):
        super().__init__(logger = logger, window = window, board = board)
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

    def handle_draw_event(self, event: EventType) -> str:
        debug = ''
        if event != EventType.DRAW_EVENT:
            debug += f'received {event} but required {EventType.DRAW_EVENT} Exit the system'
            return debug
        debug += 'Drawing object'
        return debug

    def handle_open_event(self, event: EventType) -> str:
        debug = ''
        if event != EventType.OPEN_EVENT:
            debug += f'received {event} but required {EventType.OPEN_EVENT} Exit the system'
            return debug
        debug += 'Opening the window'
        return debug
