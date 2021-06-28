#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 10:42
# @Description: ENTER DESCRIPTION HERE ...
# @Source: ENTER THE SOURCE HERE ...
#
#################################################
from cube3d.engine import GameEngine, EngineState

def make_engine_mock():
    return EngineMock()

class EngineMock(GameEngine):

    def __init__(self, fps: int = 10, window = None):
        super().__init__(fps, window)

    def start(self):
        if self.window is None:
            raise ValueError(f'Cannot start the Game Engine without the screen reference')

        if self._engine_state != EngineState.Created:
            raise ValueError(f'Cannot start engine: current engine state is {self._engine_state}')

        if self.handler is None:
            raise ValueError(f'Cannot start the Game Engine without the reference for the event handler')

        self._engine_state = EngineState.Running
        print('Opening the window')
        print('Engine is running')

    def stop(self):
        if self._engine_state != EngineState.Running:
            raise ValueError(f'Cannot stop engine: current engine state is {self._engine_state}')
        print('Closing the window')
        print('Engine is stopped')
        self._engine_state = EngineState.Destroyed

    def is_alive(self) -> bool:
        return self._engine_state == EngineState.Running
