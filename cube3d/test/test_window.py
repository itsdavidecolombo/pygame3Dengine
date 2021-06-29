#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The Window unittest script
#
#################################################
import unittest
from cube3d.screen.window import Window
from cube3d.test.loggertest import logger_mock
from cube3d.test.guardtest import guard_mock

class TestWindow(unittest.TestCase):

    def setUp(self) -> None:
        self.guard = guard_mock.make_guard_mock()
        self.logger = logger_mock.make_logger_mock(self.guard)
        self.guard.set_logger(self.logger)
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
