#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:45
# @Description: A class for checking the correct behaviour during the game loop
#
#################################################
from cube3d.engine import EngineState
import pygame
import sys

class EngineGuard:

    def __init__(self, engine = None):
        self.engine = engine

    def set_engine(self, engine) -> bool:
        if self.engine is not None:
            # TODO log warning message
            return False
        self.engine = engine
        return True

    def engine_is_ready_to_start(self) -> bool:
        if self.engine is None:
            return False

        if self.engine.window is None:
            print(f'Cannot start the Game Engine without the reference to the window object')
            return False
        elif self.engine.handler is None:
            print(f'Cannot start the Game Engine without the reference to the event handler object')
            return False
        elif self.engine.clock is None:
            print(f'Cannot start the Game Engine without the reference to the clock object')
            return False
        elif self.engine.get_engine_state() != EngineState.Created:
            print(f'Cannot start engine: current engine state is {self.engine.get_engine_state()}')
            return False
        else:
            print(f'[Engine is ready to start ...]')
            return True

    def safe_shut_down(self):
        if self.engine is not None:
            print(f'[Safe shut down the engine ...]')
            if self.engine.get_engine_state() == EngineState.Running:
                self.engine.set_stop_event()
                self.engine.set_engine_state(EngineState.Destroyed)
                self.engine.window.close()
                pygame.quit()
        sys.exit()
