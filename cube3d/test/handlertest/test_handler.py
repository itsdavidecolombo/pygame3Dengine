#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 15:53
# @Description: The unittest script for testing event handling
#
#################################################
import unittest
from cube3d.test.handlertest import handler_mock
from cube3d.event import EventType

# ================================= TEST EVENT HANDLER CLASS =================================
class TestHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = handler_mock.make_handler_mock(board = object(), logger = object(), window = object())

    def tearDown(self) -> None:
        pass

    def test_make_handler_mock(self):
        self.assertTrue(self.handler.board is not None)
        self.assertTrue(self.handler.logger is not None)
        self.assertTrue(self.handler.window is not None)

    def test_handle_draw_event(self):
        event = EventType.DRAW_EVENT
        debug_msg = self.handler.handle_events(event = event)
        self.assertTrue(debug_msg == 'Drawing objects')

    def test_open_event(self):
        event = EventType.OPEN_EVENT
        debug_msg = self.handler.handle_events(event = event)
        self.assertTrue(debug_msg == 'Opening the window')

    def test_should_safe_shut_down_when_receive_unknown_event(self):
        debug_msg = self.handler.handle_events(event = object())
        print(debug_msg)
        self.assertTrue(debug_msg == 'Unknown event Exit the system')

if __name__ == '__main__':
    unittest.main()
