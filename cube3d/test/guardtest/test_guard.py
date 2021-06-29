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
from cube3d.data_model import Cube

class TestGuard(unittest.TestCase):

    def setUp(self) -> None:
        self.guard_mock = guard_mock.make_guard_mock()
        self.clock = Clock()
        self.window = Window('test')
        self.board = GameBoard(Cube())
        self.handler_mock = handler_mock.make_handler_mock(board = self.board, guard = self.guard_mock)

    def tearDown(self) -> None:
        pass

    def test_default_guard(self):
        self.assertTrue(self.guard_mock is not None)
        self.assertTrue(self.guard_mock.engine is None)

    def test_engine_ready_to_start(self):
        self.engine_mock = engine_mock.make_engine_mock(clock = None,
                                                        window = self.window,
                                                        guard = self.guard_mock,
                                                        handler = self.handler_mock)
        self.guard_mock.set_engine(self.engine_mock)
        is_ready = self.guard_mock.engine_is_ready_to_start()
        self.assertFalse(is_ready)

    def test_should_not_stop_engine_when_not_started(self):
        self.engine_mock = engine_mock.make_engine_mock(clock = self.clock,
                                                        window = self.window,
                                                        guard = self.guard_mock,
                                                        handler = self.handler_mock)
        self.guard_mock.set_engine(self.engine_mock)
        debug_msg = self.guard_mock.safe_shut_down()
        self.assertTrue(debug_msg == 'Exit the system')

    def test_safe_shut_down(self):
        self.engine_mock = engine_mock.make_engine_mock(clock = self.clock,
                                                        window = self.window,
                                                        guard = self.guard_mock,
                                                        handler = self.handler_mock)
        self.guard_mock.set_engine(self.engine_mock)
        is_started = self.engine_mock.start()
        self.assertTrue(is_started)
        debug_msg = self.guard_mock.safe_shut_down()
        self.assertTrue(debug_msg == 'Stopping the engine Change engine state Closing the window Quitting pygame Exit the system')

    def test_set_none_engine(self):
        self.engine_mock = engine_mock.make_engine_mock(clock = self.clock,
                                                        window = self.window,
                                                        guard = self.guard_mock,
                                                        handler = self.handler_mock)
        self.guard_mock.set_engine(None)
        debug = self.engine_mock.start()
        self.assertTrue(debug == 'Exit the system')

    def test_should_return_false_when_set_twice(self):
        self.engine_mock = engine_mock.make_engine_mock(clock = self.clock,
                                                        window = self.window,
                                                        guard = self.guard_mock,
                                                        handler = self.handler_mock)
        is_set = self.guard_mock.set_engine(self.engine_mock)
        self.assertTrue(is_set)
        is_set = self.guard_mock.set_engine(self.engine_mock)
        self.assertFalse(is_set)



if __name__ == '__main__':
    unittest.main()
