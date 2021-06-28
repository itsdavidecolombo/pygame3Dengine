#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:42
# @Description: The EngineMock class that fakes the implementations of the start and stop methods of the Game Engine
#               for making testing simpler without using threads that have an unpredictable behaviour.
#
#################################################
from cube3d.engine import GameEngine, EngineState

def make_engine_mock():
    return EngineMock()

class EngineMock(GameEngine):

    def __init__(self, window = None, clock = None):
        super().__init__(clock = clock, window = window)

    def set_guard(self, guard_mock):
        self.guard = guard_mock

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
        debug = ''
        if self._engine_state != EngineState.Running:
            raise ValueError(f'Cannot stop engine: current engine state is {self._engine_state}')
        debug += 'Stopping the engine '
        self._engine_state = EngineState.Destroyed
        return debug

    def is_alive(self) -> bool:
        return self._engine_state == EngineState.Running
