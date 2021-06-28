#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine class
#
#################################################
from enum import Enum
import threading
import time
import pygame
import sys
from cube3d.screen import Window
from cube3d.engine import EventHandler

class EngineState(Enum):
    Created = 'created'
    Running = 'running'
    Destroyed = 'destroyed'

############################## GAME ENGINE CLASS ##############################
class GameEngine(threading.Thread):

    def __init__(self, fps: int = 30, window: Window = None, handler: EventHandler = None):
        super().__init__()
        self.handler = handler
        self.window  = window
        self._fps    = fps
        self._tick_length_nanoseconds = int((1 / fps) * 1e9)
        self._elapsed_nanoseconds = time.time_ns()
        self._engine_state = EngineState.Created
        self._stop_event   = threading.Event()

    def set_fps(self, fps: int) -> None:
        self._fps = fps
        self._tick_length_nanoseconds = int((1 / fps) * 1e9)

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
        if self._engine_state != EngineState.Running:
            raise ValueError(f'Cannot stop engine: current engine state is {self._engine_state}')
        self._stop_event.set()
        self._engine_state = EngineState.Destroyed

    def start(self):
        if self.window is None:
            raise ValueError(f'Cannot start the Game Engine without the reference for the screen')

        if self.handler is None:
            raise ValueError(f'Cannot start the Game Engine without the reference for the event handler')

        if self._engine_state != EngineState.Created:
            raise ValueError(f'Cannot start engine: current engine state is {self._engine_state}')

        self.__init_and_run()

    def __init_and_run(self):
        pygame.init()
        self.__DISPLAY = self.window.open()
        self._engine_state = EngineState.Running
        self.run()

    def run(self):
        while not self._stop_event.is_set():
            if self._elapsed_nanoseconds < self._tick_length_nanoseconds:
                time.sleep(float(self._tick_length_nanoseconds - self._elapsed_nanoseconds) / 1e9)
            self.__on_clock_tick()
        self.__safe_shut_down()
        return

    def __safe_shut_down(self):
        self.window.close()
        pygame.quit()
        sys.exit()

    def __on_clock_tick(self):
        start_nanoseconds = time.time_ns()

        # Handling all the events
        self.handler.handle_events()

        # Update Objects


        # Draw Objects
        self.__DISPLAY.fill(Window.BLACK)

        # TODO call UIDelegate (return True or False)

        # Update display
        pygame.display.update()
        self._elapsed_nanoseconds = (time.time_ns() - start_nanoseconds)
