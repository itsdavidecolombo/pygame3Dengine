#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 16:43
# @Description: The guard mock class for faking the implementation of stop method and allow easy testing
#
#################################################
from cube3d.engine import EngineGuard

def make_guard_mock():
    return GuardMock()

class GuardMock(EngineGuard):

    def __init__(self, engine = None):
        super().__init__(engine)

    def set_logger(self, logger):
        self.logger = logger

    def safe_shut_down(self) -> str:
        debug = ''
        if self.engine is not None:
            if self.engine.is_alive():
                debug += 'Stopping the engine '
                debug += 'Change engine state '
                debug += 'Closing the window '
                debug += 'Quitting pygame '
        debug += 'Exit the system'
        return debug
