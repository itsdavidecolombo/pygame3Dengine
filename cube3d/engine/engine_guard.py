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

    # TODO remove set engine and force engine in constructor
    def set_engine(self, engine):
        if self.engine is not None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: engine is not None...')
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Setting the engine...')
        self.engine = engine

    def set_logger(self, logger):
        if self.logger is not None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: logger is not None...')
        self.logger = logger
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Setting the logger...')

    def safe_start(self):
        if self.logger is None:
            raise ValueError(f'EngineGuard: cannot start the application without a valid logger...')
        if self.engine is None:
            raise ValueError(f'EngineGuard: cannot start the application without a valid engine...')

        self.__check_engine()
        self.__start_engine()

    def __check_engine(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Checking engine before starting...')
        if self.engine.window is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: window is None...')
        elif self.engine.handler is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: event handler is None...')
        elif self.engine.clock is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: clock is None...')
        elif self.engine.is_alive():
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: engine is already started...')
        elif self.engine.is_stopped():
            self.logger.log(level = LoggerLevel.Severe, msg = 'EngineGuard: engine is already stopped...')
        else:
            self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: engine is ready to start...')

    def __start_engine(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Starting the engine...')
        pygame.init()
        # self.__DISPLAY = self.window.open()
        self.engine.set_engine_state(EngineState.Running)
        self.engine.run()

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
