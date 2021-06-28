#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine class
#
#################################################
import threading
import time
import pygame
from cube3d.screen import Window
from cube3d.event import EventHandler
from cube3d.engine import Clock, EngineState, EngineGuard

############################## GAME ENGINE CLASS ##############################
class GameEngine(threading.Thread):

    def __init__(self,
                 clock: Clock = None,
                 window: Window = None,
                 handler: EventHandler = None):
        super().__init__()
        self.handler = handler
        self.window  = window
        self.clock   = clock
        self.guard   = EngineGuard(self)
        self._elapsed_nanoseconds = time.time_ns()
        self._engine_state = EngineState.Created
        self._stop_event   = threading.Event()

    def set_clock(self, clock: Clock) -> bool:
        if self.clock is not None:
            raise ValueError(f'Game Engine already has a reference to Clock object')
        self.clock = clock
        return True

    def set_window(self, window: Window) -> bool:
        if self.window is not None:
            raise ValueError(f'Game Engine already has a reference to the screen')
        self.window = window
        return True

    def set_event_handler(self, handler: EventHandler) -> bool:
        if self.handler is not None:
            raise ValueError(f'Event handler is already assigned to the Game Engine')
        self.handler = handler
        return True

    def get_engine_state(self) -> EngineState:
        return self._engine_state

    def stop(self):
        self._stop_event.set()
        self._engine_state = EngineState.Destroyed

    def start(self) -> bool:
        if not self.guard.engine_is_ready_to_start():
            self.guard.safe_shut_down()
            return False
        self.__init_and_run()
        return True

    def __init_and_run(self):
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
