#################################################
#
# @Author: davidecolombo
# @Date: mar, 29-06-2021, 10:13
# @Description: The unittest script for the logger
#
#################################################

import unittest
from cube3d.test.guardtest import guard_mock
from cube3d.test.enginetest import engine_mock
from cube3d.test.handlertest import handler_mock
from cube3d.test.loggertest import logger_mock
from cube3d.board import GameBoard
from cube3d.engine import Clock
from cube3d.data_model import Cube

class TestLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.clock = Clock(fps = 30)
        self.board = GameBoard(player = Cube())
        self.guard = guard_mock.make_guard_mock()
        self.handler = handler_mock.make_handler_mock(board = self.board, guard = self.guard)
        self.engine = engine_mock.make_engine_mock(clock = self.clock, window = None, handler = self.handler, guard = self.guard)
        self.guard.set_engine(self.engine)
        self.logger = logger_mock.make_logger_mock(self.guard)

    def tearDown(self) -> None:
        pass

    def test_make_logger(self):
        self.assertTrue(self.logger is not None)
        self.assertTrue(self.logger.guard is not None)

    def test_call_safe_shut_down_when_log_error(self):
        msg = self.logger.log(level = logger_mock.LoggerLevel.Severe, msg = 'something happen')
        self.assertTrue(msg == 'Exit the system')


if __name__ == '__main__':
    unittest.main()
