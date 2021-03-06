#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 14:43
# @Description: The unittest script for the Clock class
#
#################################################
import unittest
from cube3d.engine import Clock
from cube3d.test.loggertest import logger_mock

class TestClock(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = logger_mock.make_logger_mock(object())
        self.clock = Clock(fps = 30, logger = self.logger)

    def tearDown(self) -> None:
        pass

    def test_make_clock_with_fps(self):
        self.assertTrue(self.clock.fps == 30)
        self.assertTrue(self.clock._tick_nano == int((1 / 30) * 1e9))

    def test_should_raise_ValueError_when_set_negative_fps(self):
        try:
            Clock(fps = -10, logger = self.logger)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

        try:
            Clock(fps = None, logger = self.logger)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_should_raise_ValueError_when_logger_is_None(self):
        try:
            Clock(fps = 10, logger = None)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_compute_pausing_time_between_loop_iterations(self):
        pause = self.clock.get_pause_seconds(elapsed_nano = int(1e5))
        self.assertTrue(pause == float((int((1/float(30))*1e9) - int(1e5))/1e9))
        pause2 = self.clock.get_pause_seconds(elapsed_nano = int(1e10))
        self.assertTrue(pause2 == 0.0)


if __name__ == '__main__':
    unittest.main()
