#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 16:43
# @Description: The guard mock class for faking the implementation of stop method and allow easy testing
#
#################################################
from cube3d.engine import EngineGuard, EngineState

def make_guard_mock():
    return GuardMock()

class GuardMock(EngineGuard):

    def __init__(self, engine = None):
        super().__init__(engine)

    def set_engine(self, engine) -> str:
        debug = ''
        if self.engine is not None:
            debug += 'Engine is not None Exit the system'
            return debug
        debug += 'Setting the engine'
        self.engine = engine
        return debug

    def set_logger(self, logger) -> str:
        debug = ''
        if self.logger is not None:
            debug += 'Logger is not None Exit the system'
            return debug
        debug += 'Setting the logger'
        self.logger = logger
        return debug

    def safe_start(self) -> str:
        debug = ''
        if self.logger is None:
            debug += 'Logger is None Exit the system'
            return debug
        if self.engine is None:
            debug += 'Engine is None Exit the system'
            return debug

        debug += self.__check_engine()
        if debug.__contains__('Exit the system'):
            return debug
        debug += self.__start_engine()
        return debug

    def __check_engine(self) -> str:
        debug = 'Check engine '
        if self.engine.window is None:
            debug += 'Window is None Exit the system'
            return debug
        elif self.engine.handler is None:
            debug += 'Handler is None Exit the system'
            return debug
        elif self.engine.clock is None:
            debug += 'Clock is None Exit the system'
            return debug
        elif self.engine.is_alive():
            debug += 'Engine is running Exit the system'
            return debug
        elif self.engine.is_stopped():
            debug += 'Engine is stopped Exit the system'
            return debug
        return debug

    def __start_engine(self) -> str:
        debug = 'Starting the engine '
        debug += 'Init pygame '
        debug += 'Opening window '
        debug += 'Set running '
        debug += 'run '
        self.engine._engine_state = EngineState.Running
        return debug

    def safe_shut_down(self) -> str:
        debug = ''
        if self.engine is not None:
            if self.engine.is_alive():
                debug += 'Stopping the engine '
                debug += 'Change engine state '
                debug += 'Closing the window '
                debug += 'Quitting pygame '
                self.engine._engine_state = EngineState.Destroyed
        debug += 'Exit the system'
        return debug
