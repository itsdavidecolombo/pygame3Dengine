#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine unittest script
#
#################################################
import unittest
from cube3d.engine import EngineState, Clock
from cube3d.test.handlertest import handler_mock
from cube3d.test.enginetest import engine_mock
from cube3d.test.guardtest import guard_mock
from cube3d.test.loggertest import logger_mock
from cube3d.screen import Window

############################## GAME ENGINE TEST CLASS ##############################
class TestEngine(unittest.TestCase):

    def setUp(self) -> None:
        self.guard_mock = guard_mock.make_guard_mock()
        self.logger = logger_mock.make_logger_mock(self.guard_mock)
        self.guard_mock.set_logger(self.logger)
        self.clock = Clock(fps = 30, logger = self.logger)
        self.screen = Window(title = 'Engine Test', width = 800, height = 600, logger = self.logger)
        self.handler = handler_mock.make_handler_mock(board = None, logger = self.logger)
        self.engine  = None

    def tearDown(self) -> None:
        pass

    def test_start_and_stop_successfully(self):
        self.engine = engine_mock.make_engine_mock(clock = self.clock,
                                                   window = self.screen,
                                                   guard = self.guard_mock,
                                                   handler = self.handler)
        self.guard_mock.set_engine(self.engine)
        is_started = self.engine.start()
        self.assertTrue(is_started)
        self.assertTrue(self.engine.is_alive())
        debug_msg = self.engine.guard.safe_shut_down()
        self.assertTrue(debug_msg == 'Stopping the engine Change engine state Closing the window Quitting pygame Exit the system')

# =========================== START AND STOP TESTS ===========================
    def test_should_safe_shut_down_when_already_started(self):
        self.engine = engine_mock.make_engine_mock(clock = self.clock,
                                                   window = self.screen,
                                                   guard = self.guard_mock,
                                                   handler = self.handler)
        self.guard_mock.set_engine(self.engine)
        is_started = self.engine.start()
        self.assertTrue(is_started)
        self.assertTrue(self.engine.get_engine_state() == EngineState.Running)
        debug_msg = self.engine.start()
        self.assertTrue(debug_msg == 'Stopping the engine Change engine state Closing the window Quitting pygame Exit the system')


# =========================== SETTER TESTS ===========================
    def test_should_safe_shut_down_if_window_is_none(self):
        self.engine = engine_mock.make_engine_mock(clock = self.clock,
                                                   window = None,
                                                   guard = self.guard_mock,
                                                   handler = self.handler)
        self.guard_mock.set_engine(self.engine)
        debug = self.engine.start()
        self.assertTrue(debug == 'Exit the system')

    def test_should_safe_shut_down_if_handler_is_none(self):
        self.engine = engine_mock.make_engine_mock(clock = self.clock,
                                                   window = self.screen,
                                                   guard = self.guard_mock,
                                                   handler = None)
        self.guard_mock.set_engine(self.engine)
        debug = self.engine.start()
        self.assertTrue(debug == 'Exit the system')

    def test_should_safe_shut_down_if_clock_is_none(self):
        self.engine = engine_mock.make_engine_mock(clock = None,
                                                   window = self.screen,
                                                   guard = self.guard_mock,
                                                   handler = self.handler)
        self.guard_mock.set_engine(self.engine)
        debug = self.engine.start()
        self.assertTrue(debug == 'Exit the system')

    def test_should_set_state_consistently(self):
        self.engine = engine_mock.make_engine_mock(clock = self.clock,
                                                   window = self.screen,
                                                   guard = self.guard_mock,
                                                   handler = self.handler)
        self.guard_mock.set_engine(self.engine)
        self.engine.set_logger(self.logger)
        self.assertTrue(self.engine.get_engine_state() == EngineState.Created)
        self.assertFalse(self.engine.set_engine_state(EngineState.Created))
        self.engine.start()
        self.assertTrue(self.engine.is_alive())
        self.assertFalse(self.engine.set_engine_state(EngineState.Created))
        self.assertFalse(self.engine.set_engine_state(EngineState.Running))
        self.assertTrue(self.engine.set_engine_state(EngineState.Destroyed))


if __name__ == '__main__':
    unittest.main()
