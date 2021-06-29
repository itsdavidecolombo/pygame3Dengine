#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:43
# @Description: A unittest script for testing the engine guard class behaviour
#
#################################################
import unittest
from cube3d.test.enginetest import engine_mock
from cube3d.test.guardtest import guard_mock

class TestGuard(unittest.TestCase):

    def setUp(self) -> None:
        self.engine = engine_mock.make_engine_mock(clock = object(), window = object(), handler = object())
        self.guard_mock = guard_mock.make_guard_mock(engine = self.engine, logger = object())

    def tearDown(self) -> None:
        pass

    def test_create_guard_correctly(self):
        self.assertTrue(self.guard_mock.logger is not None)
        self.assertTrue(self.guard_mock.engine is not None)

    def test_engine_ready_to_start(self):
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Starting the engine Init pygame Opening window Set running run ')

    def test_should_not_stop_engine_when_not_started(self):
        debug_msg = self.guard_mock.safe_shut_down()
        self.assertTrue(debug_msg == 'Exit the system')

    def test_safe_shut_down(self):
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Starting the engine Init pygame Opening window Set running run ')
        debug_msg = self.guard_mock.safe_shut_down()
        self.assertTrue(debug_msg == 'Stopping the engine Change engine state Closing the window Quitting pygame Exit the system')

    def test_set_none_engine(self):
        try:
            guard_mock.make_guard_mock(engine = None, logger = object())
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_set_none_logger(self):
        try:
            guard_mock.make_guard_mock(engine = object(), logger = None)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_should_exit_if_engine_is_not_initialize_correctly(self):
        self.engine = engine_mock.make_engine_mock(clock = object(), window = None, handler = object())
        self.guard_mock = guard_mock.make_guard_mock(engine = self.engine, logger = object())
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Window is None Exit the system')

        self.engine = engine_mock.make_engine_mock(clock = None, window = object(), handler = object())
        self.guard_mock = guard_mock.make_guard_mock(engine = self.engine, logger = object())
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Clock is None Exit the system')

        self.engine = engine_mock.make_engine_mock(clock = object(), window = object(), handler = None)
        self.guard_mock = guard_mock.make_guard_mock(engine = self.engine, logger = object())
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Handler is None Exit the system')

    def test_should_exit_if_engine_is_running(self):
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Starting the engine Init pygame Opening window Set running run ')
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Engine is running Exit the system')

    def test_should_exit_if_engine_is_stopped(self):
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Starting the engine Init pygame Opening window Set running run ')
        debug_msg = self.guard_mock.safe_shut_down()
        self.assertTrue(debug_msg == 'Stopping the engine Change engine state Closing the window Quitting pygame Exit the system')
        debug_msg = self.guard_mock.safe_start()
        self.assertTrue(debug_msg == 'Check engine Engine is stopped Exit the system')


if __name__ == '__main__':
    unittest.main()
