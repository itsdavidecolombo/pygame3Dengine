#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine class
#
#################################################
import time
# TODO remove pygame import in future
import pygame
import threading
from cube3d.ui import Window
from cube3d.event import EventHandler
from cube3d.logger import Logger, LoggerLevel
from cube3d.engine import Clock, EngineState


############################## GAME ENGINE CLASS ##############################
class GameEngine(threading.Thread):

    def __init__(self, clock: Clock, window: Window, handler: EventHandler, logger: Logger):
        super().__init__()
        self.__DISPLAY = None
        self.handler = handler
        self.window  = window
        self.clock   = clock
        self.logger  = logger
        self._elapsed_nanoseconds = 0
        self._engine_state = EngineState.Created
        self._stop_event   = threading.Event()

    def set_engine_state(self, to_: EngineState):
        if not EngineState.is_allowed_state_transition(from_ = self._engine_state, to_ = to_):
            self.logger.log(level = LoggerLevel.Severe,
                            msg = f'GameEngine: cannot change engine state from {self._engine_state} to {to_}')
        self._engine_state = to_

    def set_stop_event(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameEngine: Setting stop event...')
        self._stop_event.set()

    # TODO remove this method in future
    def set_display(self, display: pygame.Surface):
        self.__DISPLAY = display

    def is_stopped(self):
        return self._engine_state == EngineState.Destroyed

    def is_alive(self) -> bool:
        return (self._engine_state == EngineState.Running) or super().is_alive()

    def run(self):
        while not self._stop_event.is_set():
            time.sleep(self.clock.get_pause_seconds(elapsed_nano = self._elapsed_nanoseconds))
            self.__on_clock_tick()
        return

    def __on_clock_tick(self):
        start_nanoseconds = time.time_ns()

        # Handling all the events
        self.handler.handle_events()

        # Update Objects

        # Draw Objects
        self.__DISPLAY.fill(Window.BLACK)

        # Update display
        pygame.display.update()
        self._elapsed_nanoseconds = (time.time_ns() - start_nanoseconds)
