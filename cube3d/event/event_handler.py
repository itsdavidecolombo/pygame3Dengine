#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 15:57
# @Description: Event Handler class for handling pygame event during game loop
#
#################################################
import pygame
from cube3d.event import EventType
from cube3d.board import GameBoard
from cube3d.ui import Window
from cube3d.logger import Logger, LoggerLevel

class EventHandler:

    def __init__(self, board: GameBoard, window: Window, logger: Logger):
        self.board  = self.__safe_init_board(board)
        self.logger = self.__safe_init_logger(logger)
        self.window = self.__safe_init_window(window)

    def __safe_init_board(self, board: GameBoard) -> GameBoard:
        if board is None:
            raise ValueError('EventHandler: cannot start the application without reference to the board...')
        return board

    def __safe_init_window(self, window: Window) -> Window:
        if window is None:
            raise ValueError('EventHandler: cannot start the application without reference to the window...')
        return window

    def __safe_init_logger(self, logger: Logger) -> Logger:
        if logger is None:
            raise ValueError('EventHandler: cannot start the application without reference to the logger...')
        return logger

    def handle_events(self, event: EventType):
        if event == EventType.CLOSE_EVENT:
            self.__handle_close_event()
        elif event == EventType.OPEN_EVENT:
            self.__handle_open_event()
        elif event == EventType.DRAW_EVENT:
            self.__handle_draw_event()
        elif event == EventType.USER_EVENT:
            self.__handle_user_events()
        else:
            self.logger.log(level = LoggerLevel.Severe,
                            msg = f'EventHandler: \'handle_events()\' method cannot handle {event} events...')

    def __handle_draw_event(self):
        pass
        # self.board.draw()

    def __handle_open_event(self):
        self.window.open()

    def __handle_close_event(self):
        self.window.close()

# ============================= USER EVENTS =============================
    def __handle_user_events(self):
        for event in pygame.event.get():
            # QUIT EVENT
            if event.type == pygame.QUIT:
                self.__quit_engine()

            # KEY DOWN EVENTS
            if event.type == pygame.KEYDOWN:
                self.__handle_key_down(event)

            # KEY UP EVENTS
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_j:
                    pass

# ============================= HANDLE KEY DOWN METHOD =============================
    def __handle_key_down(self, event):
        if event.key == pygame.K_x:
            self.board.rotate_x()
        elif event.key == pygame.K_y:
            self.board.rotate_y()
        elif event.key == pygame.K_z:
            self.board.rotate_z()
        elif event.key == pygame.K_ESCAPE:
            self.__quit_engine()

# ============================= QUIT ENGINE METHOD =============================
    def __quit_engine(self) -> bool:
        self.logger.log(level = LoggerLevel.Severe, msg = 'EventHandler: quitting the engine...')
        return False
