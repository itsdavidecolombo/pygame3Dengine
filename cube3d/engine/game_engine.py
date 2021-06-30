#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:07
# @Description: The GameEngine class
#
#################################################
import time
import threading
from cube3d.event import EventHandler, EventType
from cube3d.logger import Logger, LoggerLevel
from cube3d.engine import Clock, EngineState


############################## GAME ENGINE CLASS ##############################
class GameEngine(threading.Thread):

    def __init__(self, clock: Clock, handler: EventHandler, logger: Logger):
        super().__init__()
        self.__DISPLAY = None
        self.handler = handler
        self.clock   = clock
        self.logger  = logger
        self._elapsed_nanoseconds = 0
        self._engine_state = EngineState.Created

    def set_engine_state(self, to_: EngineState):
        if not EngineState.is_allowed_state_transition(from_ = self._engine_state, to_ = to_):
            self.logger.log(level = LoggerLevel.Severe,
                            msg = f'GameEngine: cannot change engine state from {self._engine_state} to {to_}')
        self._engine_state = to_

    # TODO synchronize access to the method
    def is_stopped(self):
        return self._engine_state == EngineState.Destroyed

    def is_alive(self) -> bool:
        return (self._engine_state == EngineState.Running) or super().is_alive()

    def fire_close_event(self):
        self.handler.handle_events(EventType.CLOSE_EVENT)

    def fire_open_event(self):
        self.handler.handle_events(EventType.OPEN_EVENT)

    def run(self):
        while not self.is_stopped():
            time.sleep(self.clock.get_pause_seconds(elapsed_nano = self._elapsed_nanoseconds))
            self.__on_clock_tick()
        return

    def __on_clock_tick(self):
        start_nanoseconds = time.time_ns()

        # Handling all the events
        self.handler.handle_events(event = EventType.USER_EVENT)

        # Rendering the objects on the screen
        self.handler.handle_events(event = EventType.DRAW_EVENT)

        # Update display
        # pygame.display.update()
        self._elapsed_nanoseconds = (time.time_ns() - start_nanoseconds)
