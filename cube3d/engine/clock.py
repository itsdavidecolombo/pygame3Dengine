#################################################
#
# @Author: davidecolombo
# @Date: lun, 28-06-2021, 14:38
# @Description: The Clock class handles the timing variables of the game loop
#
#################################################

class Clock:

    _NANO_PER_SEC = 1e9

    def __init__(self, fps: int = None):
        self.fps = fps
        self._tick_length_nanoseconds = self.__safe_init_tick_length(fps)

    def __safe_init_tick_length(self, fps: int) -> int or None:
        if fps is None:
            return None
        return self.__compute_tick_length_nanoseconds()

    def set_fps(self, fps: int):
        self.fps = fps
        self._tick_length_nanoseconds = self.__compute_tick_length_nanoseconds()

    def __compute_tick_length_nanoseconds(self):
        return int((1 / self.fps) * Clock._NANO_PER_SEC)

    def get_pause_seconds(self, elapsed_nano: int) -> float:
        if elapsed_nano < self._tick_length_nanoseconds:
            return float((self._tick_length_nanoseconds - elapsed_nano) / Clock._NANO_PER_SEC)
        return 0.0
