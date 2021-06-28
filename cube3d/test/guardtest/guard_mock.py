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

    def set_engine(self, engine_mock):
        self.engine = engine_mock

    def safe_shut_down(self) -> bool:
        print('Stopping the engine')
        print('Closing the window')
        print('Quitting pygame')
        print('Exit the system')
        return True
