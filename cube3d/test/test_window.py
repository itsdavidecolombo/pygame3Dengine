#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The Window unittest script
#
#################################################
import unittest
from cube3d.screen.window import Window

class TestWindow(unittest.TestCase):

    def setUp(self) -> None:
        self.window = Window(' ')

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

    def test_open_window_ValueError_already_opened(self):
        self.window.open()
        try:
            self.window.open()
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_close_window(self):
        self.assertFalse(self.window.is_opened())
        self.window.open()
        self.assertTrue(self.window.is_opened())
        self.window.close()
        self.assertFalse(self.window.is_opened())

    def test_close_window_ValueError_not_opened(self):
        try:
            self.window.close()
            self.fail()
        except ValueError as ex:
            print(ex.__str__())


if __name__ == '__main__':
    unittest.main()
