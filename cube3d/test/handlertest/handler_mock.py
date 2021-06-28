#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:47
# @Description: ENTER DESCRIPTION HERE ...
# @Source: ENTER THE SOURCE HERE ...
#
#################################################
from cube3d.engine import EventHandler

def make_handler_mock(board, guard):
    return EventHandlerMock(events = [], board = board, guard = guard)

class EventHandlerMock(EventHandler):
    QUIT = 'quit'
    OK   = 'ok'

    def __init__(self, events: list[str], board, guard):
        super().__init__(guard, board)
        self.events = events

    def handle_events(self, events: list[str] = None) -> str:
        if events is not None:
            self.events = events
        for event in self.events:
            if event == EventHandlerMock.QUIT:
                self.guard.safe_shut_down()
                return 'quit_event'
            elif event == EventHandlerMock.OK:
                feed = True
                feed = feed and self.board.rotate_x()
                feed = feed and self.board.rotate_y()
                feed = feed and self.board.rotate_z()
                if feed:
                    return 'ok_event'
                else:
                    return 'quit_event'
