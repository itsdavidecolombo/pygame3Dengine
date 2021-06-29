#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:45
# @Description: A class for checking the correct behaviour during the game loop
#
#################################################
from cube3d.engine import EngineState
import logging
import pygame
import sys

class EngineGuard:

    def __init__(self, engine = None):
        self.engine = engine

    def set_engine(self, engine) -> bool:
        if self.engine is not None:
            logging.log(level = logging.WARNING, msg = f'Cannot set engine: engine is not None')
            return False
        self.engine = engine
        return True

    def engine_is_ready_to_start(self) -> bool:
        if self.engine is None:
            return False

        if self.engine.window is None:
            logging.log(level = logging.WARNING,
                        msg = f'Cannot start the Game Engine without the reference to the window object')
            return False
        elif self.engine.handler is None:
            logging.log(level = logging.WARNING,
                        msg = f'Cannot start the Game Engine without the reference to the header object')
            return False
        elif self.engine.clock is None:
            logging.log(level = logging.WARNING,
                        msg = f'Cannot start the Game Engine without the reference to the clock object')
            return False
        elif self.engine.is_alive() or self.engine.is_stopped():
            logging.log(level = logging.WARNING,
                        msg = f'Cannot start the Game Engine when already alive or just stopped')
            return False
        else:
            logging.debug(msg = f'Engine is ready to start')
            return True

    def safe_shut_down(self):
        debug = ''
        if self.engine is not None:
            if self.engine.is_alive():
                debug += 'Safe shut down the engine and '
                self.engine.set_stop_event()
                self.engine.set_engine_state(to_ = EngineState.Destroyed)
                self.engine.window.close()
                pygame.quit()
        debug += 'exit the system'
        logging.debug(msg = debug)
        sys.exit()
