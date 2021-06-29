#################################################
#
# @Author: davidecolombo
# @Date: mar, 29-06-2021, 10:13
# @Description: The unittest script for the logger
#
#################################################

import unittest
from cube3d.test.loggertest import logger_mock

class TestLogger(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = logger_mock.make_logger_mock(object())

    def tearDown(self) -> None:
        pass

    def test_should_exit_when_guard_is_none(self):
        try:
            logger_mock.make_logger_mock(None)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())


    def test_should_exit_when_receive_severe_log(self):
        log = self.logger.log(level = logger_mock.LoggerLevel.Severe, msg = 'something happen')
        self.assertTrue(log == 'Level Severe received Exit the system')

    def test_should_log_messages_when_not_severe(self):
        log = self.logger.log(level = logger_mock.LoggerLevel.Warning, msg = 'warning')
        self.assertTrue(log == 'warning')
        log = self.logger.log(level = logger_mock.LoggerLevel.Debug, msg = 'debug')
        self.assertTrue(log == 'debug')
        log = self.logger.log(level = logger_mock.LoggerLevel.Info, msg = 'info')
        self.assertTrue(log == 'info')


if __name__ == '__main__':
    unittest.main()
