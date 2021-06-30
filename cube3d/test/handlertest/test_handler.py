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

    def test_ok_event_handling(self):
        events = ['ok', 'ok', 'ok']
        debug_msg = self.handler.handle_events(events)
        self.assertTrue(debug_msg == 'Ok event received Ok event received Ok event received ')

    def test_quit_event_handling(self):
        events = ['ok', 'quit', 'ok']
        debug_msg = self.handler.handle_events(events)
        self.assertTrue(debug_msg == 'Ok event received Quit event Exit the system')

    def test_handle_draw_event(self):
        event = EventType.DRAW_EVENT
        debug_msg = self.handler.handle_draw_event(event)
        self.assertTrue(debug_msg == 'Drawing object')

    def test_should_safe_shut_down_when_receive_not_draw_event(self):
        event = EventType.CLOSE_EVENT
        debug_msg = self.handler.handle_draw_event(event)
        self.assertTrue(debug_msg == 'received EventType.CLOSE_EVENT but required EventType.DRAW_EVENT Exit the system')

    def test_open_event(self):
        event = EventType.OPEN_EVENT
        debug_msg = self.handler.handle_open_event(event)
        self.assertTrue(debug_msg == 'Opening the window')

    def test_should_safe_shut_down_when_receive_not_open_event(self):
        event = EventType.CLOSE_EVENT
        debug_msg = self.handler.handle_open_event(event)
        self.assertTrue(debug_msg == 'received EventType.CLOSE_EVENT but required EventType.OPEN_EVENT Exit the system')

if __name__ == '__main__':
    unittest.main()
