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

    def __init__(self, engine):
        self.engine = engine

    def engine_is_ready_to_start(self) -> bool:
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
        print(f'[Safe shut down the engine ...]')
        if self.engine.get_engine_state() == EngineState.Running:
            self.engine.stop()
            self.engine.window.close()
            pygame.quit()
        sys.exit()
