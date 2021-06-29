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
from cube3d.screen import Window

class TestLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.guard = guard_mock.make_guard_mock()
        self.logger = logger_mock.make_logger_mock(self.guard)
        self.guard.set_logger(self.logger)
        self.clock = Clock(fps = 30, logger = self.logger)
        self.board = GameBoard(player = Cube(), logger = self.logger)
        self.handler = handler_mock.make_handler_mock(board = self.board, logger = self.logger)
        self.engine = engine_mock.make_engine_mock(clock = self.clock,
                                                   window = Window(title = 'test', logger = self.logger),
                                                   handler = self.handler,
                                                   guard = self.guard)
        self.guard.set_engine(self.engine)

    def tearDown(self) -> None:
        pass

    def test_call_safe_shut_down_when_log_severe(self):
        msg = self.logger.log(level = logger_mock.LoggerLevel.Severe, msg = 'something happen')
        self.assertTrue(msg == 'Exit the system')

    def test_safe_shut_down_the_engine(self):
        self.engine.start()
        self.assertTrue(self.engine.is_alive())
        msg = self.logger.log(level = logger_mock.LoggerLevel.Severe, msg = 'something happen')
        self.assertTrue(msg == 'Stopping the engine Change engine state Closing the window Quitting pygame Exit the system')


if __name__ == '__main__':
    unittest.main()
