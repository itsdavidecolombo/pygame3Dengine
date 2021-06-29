#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine unittest script
#
#################################################
import unittest
from cube3d.engine import EngineState
from cube3d.test.enginetest import engine_mock
from cube3d.test.guardtest import guard_mock

############################## GAME ENGINE TEST CLASS ##############################
class TestEngine(unittest.TestCase):

    def setUp(self) -> None:
        self.engine  = engine_mock.make_engine_mock(clock = object(), window = object(), handler = object())
        self.guard = guard_mock.make_guard_mock(engine = self.engine, logger = object())

    def tearDown(self) -> None:
        pass

    def test_should_set_state_consistently(self):
        self.assertTrue(self.engine.get_engine_state() == EngineState.Created)
        debug_msg = self.engine.set_engine_state(EngineState.Created)
        self.assertTrue(debug_msg == 'Error changing state Exit the system')
        debug_msg = self.guard.safe_start()
        self.assertTrue(debug_msg == 'Check engine Starting the engine Init pygame Opening window Set running run ')
        self.assertTrue(self.engine.is_alive())
        debug_msg = self.engine.set_engine_state(EngineState.Created)
        self.assertTrue(debug_msg == 'Error changing state Exit the system')
        debug_msg = self.engine.set_engine_state(EngineState.Running)
        self.assertTrue(debug_msg == 'Error changing state Exit the system')
        debug_msg = self.engine.set_engine_state(EngineState.Destroyed)
        self.assertTrue(debug_msg == 'New state is EngineState.Destroyed')


if __name__ == '__main__':
    unittest.main()
