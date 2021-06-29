#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 14:38
# @Description: The Clock class handles the timing variables of the game loop
#
#################################################
from cube3d.logger import Logger, LoggerLevel

class Clock:

    _NANO_PER_SEC = 1e9

    def __init__(self, logger: Logger, fps: int = None):
        self.logger = logger
        self.fps    = fps
        self._tick_length_nanoseconds = self.__safe_init_tick_length(fps)

    def __safe_init_tick_length(self, fps: int) -> int:
        if fps is None:
            self.logger.log(level = LoggerLevel.Severe, msg = f'Clock: cannot start the application if fps is None...')
        return self.__compute_tick_length_nanoseconds()

    def set_fps(self, fps: int):
        self.logger.log(level = LoggerLevel.Debug, msg = f'Clock: set fps to {fps}...')
        self.fps = fps
        self._tick_length_nanoseconds = self.__compute_tick_length_nanoseconds()

    def __compute_tick_length_nanoseconds(self):
        return int((1 / self.fps) * Clock._NANO_PER_SEC)

    def get_pause_seconds(self, elapsed_nano: int) -> float:
        if elapsed_nano < self._tick_length_nanoseconds:
            return float((self._tick_length_nanoseconds - elapsed_nano) / Clock._NANO_PER_SEC)
        return 0.0
