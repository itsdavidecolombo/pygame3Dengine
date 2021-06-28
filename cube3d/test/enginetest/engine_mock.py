#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:42
# @Description: The EngineMock class that fakes the implementations of the start and stop methods of the Game Engine
#               for making testing simpler without using threads that have an unpredictable behaviour.
#
#################################################
from cube3d.engine import GameEngine, EngineState

def make_engine_mock(clock, window, guard, handler):
    return EngineMock(clock = clock, window = window, guard = guard, handler = handler)

class EngineMock(GameEngine):

    def __init__(self, window = None, clock = None, guard = None, handler = None):
        super().__init__(clock = clock, window = window, guard = guard, handler = handler)

    def start(self) -> str:
        debug = ''
        if not self.guard.engine_is_ready_to_start():
            return self.guard.safe_shut_down()
        self._engine_state = EngineState.Running
        debug += 'Init pygame '
        debug += 'Opening the window '
        debug += 'Engine is running'
        return debug

    def stop(self) -> str:
        return self.guard.safe_shut_down()

    def is_alive(self) -> bool:
        return self._engine_state == EngineState.Running
