#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The Window unittest script
#
#################################################
import unittest
from cube3d.ui.window import Window
from cube3d.test.loggertest import logger_mock

class TestWindow(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = logger_mock.make_logger_mock(object())
        self.window = Window(title = ' ', logger = self.logger)

    def tearDown(self) -> None:
        pass

    def test_open_and_setup_window(self):
        width = 800
        height = 600
        title = "a title"
        self.window.set_size(width, height)
        self.window.set_title(title)
        self.assertTrue(self.window.width == width)
        self.assertTrue(self.window.height == height)
        self.assertTrue(self.window.title == title)
        self.assertFalse(self.window.is_opened())

    def test_should_raise_ValueError_when_dimensions_are_negative_or_zero(self):
        self.logger = logger_mock.make_logger_mock(object())
        try:
            Window(title = ' ', logger = self.logger, width = -10)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

        try:
            Window(title = ' ', logger = self.logger, height = -10)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_should_raise_ValueError_when_logger_is_None(self):
        try:
            Window(title = ' ', logger = None)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_open_window(self):
        self.window.open()
        self.assertTrue(self.window.is_opened())

    def test_close_window(self):
        self.assertFalse(self.window.is_opened())
        self.window.open()
        self.assertTrue(self.window.is_opened())
        self.window.close()
        self.assertFalse(self.window.is_opened())


if __name__ == '__main__':
    unittest.main()
