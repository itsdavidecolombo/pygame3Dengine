#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:42
# @Description: The EngineMock class that fakes the implementations of the start and stop methods of the Game Engine
#               for making testing simpler without using threads that have an unpredictable behaviour.
#
#################################################
from cube3d.engine import GameEngine, EngineState

def make_engine_mock(clock, handler):
    return EngineMock(clock = clock, handler = handler)

class EngineMock(GameEngine):

    def __init__(self, clock = None, handler = None, logger = None):
        super().__init__(clock = clock, handler = handler, logger = logger)

    def get_engine_state(self) -> EngineState:
        return self._engine_state

    def set_engine_state(self, to_: EngineState) -> str:
        debug = ''
        if not EngineState.is_allowed_state_transition(self._engine_state, to_):
            debug += 'Error changing state Exit the system'
            return debug
        self._engine_state = to_
        debug += f'New state is {to_}'
        return debug

    def is_alive(self) -> bool:
        return self._engine_state == EngineState.Running

    def fire_close_event(self) -> str:
        return 'Close event fired'

    def fire_open_event(self) -> str:
        return 'Open event fired'
