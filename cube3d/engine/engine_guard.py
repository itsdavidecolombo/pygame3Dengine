#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 15:45
# @Description: A class for checking the correct behaviour during the game loop
#
#################################################
from cube3d.engine import EngineState, GameEngine
from cube3d.logger import Logger, LoggerLevel
import sys

class EngineGuard:

    def __init__(self, engine: GameEngine, logger: Logger):
        self.engine = self.__safe_init_engine(engine)
        self.logger = self.__safe_init_logger(logger)

    def __safe_init_logger(self, logger: Logger) -> Logger:
        if logger is None:
            raise ValueError('EngineGuard: cannot start application when logger is None...')
        return logger

    def __safe_init_engine(self, engine: GameEngine):
        if engine is None:
            raise ValueError('EngineGuard: cannot start application when engine is None...')
        return engine

    def safe_start(self):
        self.__check_engine()
        self.__start_engine()

    def __check_engine(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Checking engine before starting...')
        if self.engine.handler is None:
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
        self.engine.fire_open_event()
        self.engine.set_engine_state(EngineState.Running)
        self.engine.run()

    def safe_shut_down(self):
        if self.engine is not None:
            if self.engine.is_alive():
                self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Safe shut down the engine...')
                self.engine.set_engine_state(to_ = EngineState.Destroyed)
                self.engine.fire_close_event()
        self.logger.log(level = LoggerLevel.Debug, msg = 'EngineGuard: Exit the system...')
        sys.exit()
