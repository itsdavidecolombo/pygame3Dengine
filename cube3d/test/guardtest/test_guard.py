#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:43
# @Description: A unittest script for testing the engine guard class behaviour
#
#################################################
import unittest
from cube3d.test.enginetest import engine_mock
from cube3d.test.handlertest import handler_mock
from cube3d.test.guardtest import guard_mock
from cube3d.screen import Window
from cube3d.board import GameBoard
from cube3d.engine import Clock

class TestGuard(unittest.TestCase):

    def setUp(self) -> None:
        self.engine_mock = engine_mock.make_engine_mock()
        self.guard_mock  = guard_mock.make_guard_mock()
        self.guard_mock.set_engine(self.engine_mock)
        self.engine_mock.set_guard(self.guard_mock)
        self.board = GameBoard(self.engine_mock)
        self.handler_mock = handler_mock.make_handler_mock(self.board, self.engine_mock)

    def tearDown(self) -> None:
        pass

    def test_default_guard(self):
        self.assertTrue(self.guard_mock is not None)
        self.assertTrue(self.guard_mock.engine is not None)

    def test_engine_ready_to_start(self):
        is_ready = self.guard_mock.engine_is_ready_to_start()
        self.assertFalse(is_ready)

    def test_safe_shut_down(self):
        self.engine_mock.set_window(Window('test'))
        self.engine_mock.set_event_handler(self.handler_mock)
        self.engine_mock.set_clock(Clock(fps = 30))
        is_started = self.engine_mock.start()
        self.assertTrue(is_started)
        is_stopped = self.guard_mock.safe_shut_down()
        self.assertTrue(is_stopped)

if __name__ == '__main__':
    unittest.main()
