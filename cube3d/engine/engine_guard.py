#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:45
# @Description: A class for checking the correct behaviour during the game loop
#
#################################################
from cube3d.engine import EngineState
from cube3d.logger import Logger, LoggerLevel
import pygame
import sys

class EngineGuard:

    def __init__(self, engine = None, logger: Logger = None):
        self.engine = engine
        self.logger = logger

    def set_engine(self, engine) -> bool:
        if self.engine is not None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: engine is not None...')
            return False
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Setting the engine...')
        self.engine = engine
        return True

    def set_logger(self, logger) -> bool:
        if self.logger is not None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: logger is not None...')
            return False

        if logger is None:
            raise ValueError(f'EngineGuard: cannot start the application without a valid logger...')

        self.logger = logger
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Setting the logger...')
        return True

    def engine_is_ready_to_start(self) -> bool:
        if self.engine is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: engine is None...')
            return False

        if self.engine.window is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: window is None...')
            return False
        elif self.engine.handler is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: event handler is None...')
            return False
        elif self.engine.clock is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: clock is None...')
            return False
        elif self.engine.is_alive():
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: engine is already started...')
            return False
        elif self.engine.is_stopped():
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: engine is already stopped...')
            return False
        else:
            self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: engine is ready to start...')
            return True

    def safe_shut_down(self):
        if self.engine is not None:
            if self.engine.is_alive():
                self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Safe shut down the engine...')
                self.engine.set_stop_event()
                self.engine.set_engine_state(to_ = EngineState.Destroyed)
                self.engine.window.close()
                pygame.quit()
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Exit the system...')
        sys.exit()
