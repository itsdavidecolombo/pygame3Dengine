#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 15:53
# @Description: The unittest script for testing event handling
#
#################################################
import unittest
from cube3d.test.handlertest import handler_mock

# ================================= TEST EVENT HANDLER CLASS =================================
class TestHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.handler = handler_mock.make_handler_mock(board = object(), logger = object())

    def tearDown(self) -> None:
        pass

    def test_make_handler_mock(self):
        self.assertTrue(self.handler.board is not None)
        self.assertTrue(self.handler.logger is not None)

    def test_ok_event_handling(self):
        events = ['ok', 'ok', 'ok']
        debug_msg = self.handler.handle_events(events)
        self.assertTrue(debug_msg == 'Ok event received Ok event received Ok event received ')

    def test_quit_event_handling(self):
        events = ['ok', 'quit', 'ok']
        debug_msg = self.handler.handle_events(events)
        self.assertTrue(debug_msg == 'Ok event received Quit event Exit the system')


if __name__ == '__main__':
    unittest.main()
