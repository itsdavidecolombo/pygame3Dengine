#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine unittest script
#
#################################################
import unittest
from cube3d.engine import EngineState
from cube3d.test.handlertest import handler_mock
from cube3d.test.enginetest import engine_mock
from cube3d.screen import Window

############################## GAME ENGINE TEST CLASS ##############################
class TestEngine(unittest.TestCase):

    def setUp(self) -> None:
        self.engine  = engine_mock.make_engine_mock()
        self.screen  = Window('Engine Test', width = 800, height = 600)
        self.handler = handler_mock.make_handler_mock(board = None, engine = self.engine)

    def tearDown(self) -> None:
        if self.engine.is_alive():
            self.engine.stop()

    def test_create_engine(self):
        self.engine.set_fps(30)
        self.engine.set_window(self.screen)
        self.engine.set_event_handler(self.handler)
        self.engine.start()
        self.assertTrue(self.engine.get_engine_state() == EngineState.Running)
        self.engine.stop()
        self.assertTrue(self.engine.get_engine_state() == EngineState.Destroyed)

    def test_start_engine_ValueError_already_started(self):
        self.engine.set_window(self.screen)
        self.engine.set_event_handler(self.handler)
        self.engine.start()
        self.assertTrue(self.engine.get_engine_state() == EngineState.Running)
        try:
            self.engine.start()
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_start_engine_ValueError_window_missing(self):
        try:
            self.engine.start()
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_stop_engine_ValueError(self):
        try:
            self.engine.stop()
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_set_screen_ref(self):
        is_set = self.engine.set_window(self.screen)
        self.assertTrue(is_set)

    def test_set_screen_ref_ValueError(self):
        is_set = self.engine.set_window(self.screen)
        self.assertTrue(is_set)
        try:
            self.engine.set_window(self.screen)
        except ValueError as ex:
            print(ex.__str__())

    def test_set_event_handler(self):
        is_set = self.engine.set_event_handler(self.handler)
        self.assertTrue(is_set)

    def test_set_event_handler_ValueError_already_set(self):
        is_set = self.engine.set_event_handler(self.handler)
        self.assertTrue(is_set)
        try:
            self.engine.set_event_handler(self.handler)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_start_ValueError_missing_handler(self):
        self.engine.set_window(self.screen)
        self.engine.set_fps(30)
        try:
            self.engine.start()
            self.fail()
        except ValueError as ex:
            print(ex.__str__())


if __name__ == '__main__':
    unittest.main()
