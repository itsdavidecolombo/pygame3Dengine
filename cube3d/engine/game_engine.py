#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine class
#
#################################################
import time
import pygame
import threading
from cube3d.screen import Window
from cube3d.event import EventHandler
from cube3d.logger import Logger, LoggerLevel
from cube3d.engine import Clock, EngineState, EngineGuard


############################## GAME ENGINE CLASS ##############################
class GameEngine(threading.Thread):

    def __init__(self,
                 clock: Clock,
                 window: Window,
                 guard: EngineGuard,
                 handler: EventHandler,
                 logger: Logger):
        super().__init__()
        self.handler = handler
        self.window = window
        self.clock  = clock
        self.guard  = guard
        self.logger = logger
        self._elapsed_nanoseconds = time.time_ns()
        self._engine_state = EngineState.Created
        self._stop_event = threading.Event()

    def set_engine_state(self, to_: EngineState) -> bool:
        if not EngineState.is_allowed_state_transition(from_ = self._engine_state, to_ = to_):
            self.logger.log(level = LoggerLevel.Severe,
                            msg = f'GameEngine: cannot change engine state from {self._engine_state} to {to_}')
            return False
        self._engine_state = to_
        return True

    # TODO all but the guard to call this method
    def set_stop_event(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameEngine: Setting stop event...')
        self._stop_event.set()

    def is_stopped(self):
        return self._engine_state == EngineState.Destroyed

    def start(self) -> bool:
        if not self.guard.engine_is_ready_to_start():
            self.guard.safe_shut_down()
            return False
        self.__init_and_run()
        return True

    def is_alive(self) -> bool:
        return (self._engine_state == EngineState.Running) or super().is_alive()

    def __init_and_run(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameEngine: Starting the engine...')
        pygame.init()
        self.__DISPLAY = self.window.open()
        self._engine_state = EngineState.Running
        self.run()

    def run(self):
        while not self._stop_event.is_set():
            time.sleep(self.clock.get_pause_seconds(elapsed_nano = self._elapsed_nanoseconds))
            self.__on_clock_tick()
        self.guard.safe_shut_down()
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
