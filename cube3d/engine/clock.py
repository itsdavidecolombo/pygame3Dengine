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

    def __init__(self, logger: Logger, fps: int):
        self.logger = self.__safe_init_logger(logger)
        self.fps    = self.__safe_init_fps(fps)
        self._tick_length_nanoseconds = self.__compute_tick_length_nanoseconds()

    def __safe_init_logger(self, logger: Logger) -> Logger:
        if logger is None:
            raise ValueError('Clock: cannot start the application without a valid reference to the logger...')
        return logger

    def __safe_init_fps(self, fps: int) -> int:
        if fps is None:
            raise ValueError('Clock: cannot start the application without setting the fps...')
        if fps <= 0:
            raise ValueError(f'Clock: \'{fps}\' is an invalid value for fps...')
        return fps

    def __compute_tick_length_nanoseconds(self):
        return int((1/float(self.fps)) * Clock._NANO_PER_SEC)

    def get_pause_seconds(self, elapsed_nano: int) -> float:
        if elapsed_nano > self._tick_length_nanoseconds*10:
            self.logger.log(level = LoggerLevel.Severe, msg = 'Clock: elapsed time is too higher, need to reduce fps...')

        if elapsed_nano < self._tick_length_nanoseconds*10:
            return float((self._tick_length_nanoseconds - elapsed_nano) / Clock._NANO_PER_SEC)
        else:
            return 0.0
