#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 15:53
# @Description: The unittest script for testing event handling
#
#################################################
import unittest
from cube3d.board import GameBoard
from cube3d.test.enginetest import engine_mock
from cube3d.test.handlertest import handler_mock

# ================================= TEST EVENT HANDLER CLASS =================================
class TestHandler(unittest.TestCase):

    def setUp(self) -> None:
        self.engine  = engine_mock.make_engine_mock()
        self.board   = GameBoard(self.engine)
        self.handler = handler_mock.make_handler_mock(self.board, self.engine)

    def tearDown(self) -> None:
        pass

    def test_make_handler_mock(self):
        self.assertTrue(self.handler is not None)
        self.assertTrue(self.handler.board is not None)

    def test_ok_event_handling(self):
        events = ['ok']
        res = self.handler.handle_events(events)
        self.assertTrue(res == 'ok_event')

    def test_quit_event_handling(self):
        events = ['quit']
        res = self.handler.handle_events(events)
        self.assertTrue(res == 'quit_event')


if __name__ == '__main__':
    unittest.main()
