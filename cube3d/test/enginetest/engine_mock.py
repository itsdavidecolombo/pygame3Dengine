#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:42
# @Description: The EngineMock class that fakes the implementations of the start and stop methods of the Game Engine
#               for making testing simpler without using threads that have an unpredictable behaviour.
#
#################################################
from cube3d.engine import GameEngine, EngineState

def make_engine_mock(clock, window, handler):
    return EngineMock(clock = clock, window = window, handler = handler)

class EngineMock(GameEngine):

    def __init__(self, window = None, clock = None, handler = None, logger = None):
        super().__init__(clock = clock, window = window, handler = handler, logger = logger)

    def get_engine_state(self) -> EngineState:
        return self._engine_state

    def is_alive(self) -> bool:
        return self._engine_state == EngineState.Running
