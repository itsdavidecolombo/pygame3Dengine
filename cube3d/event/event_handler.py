#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 15:57
# @Description: Event Handler class for handling pygame event during game loop
#
#################################################
import pygame
from cube3d.board import GameBoard
from cube3d.engine import EngineGuard

class EventHandler:

    def __init__(self, guard: EngineGuard, board: GameBoard):
        self.guard  = guard
        self.board  = board

    def handle_events(self) -> bool:
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

        return True

# ============================= HANDLE KEY DOWN METHOD =============================
    def __handle_key_down(self, event):
        feed = True
        if event.key == pygame.K_x:
            feed = feed and self.board.rotate_x()
        elif event.key == pygame.K_y:
            feed = feed and self.board.rotate_y()
        elif event.key == pygame.K_z:
            feed = feed and self.board.rotate_z()
        elif event.key == pygame.K_ESCAPE:
            self.__quit_engine()

        if not feed:
            self.__quit_engine()

# ============================= QUIT ENGINE METHOD =============================
    def __quit_engine(self) -> bool:
        self.guard.safe_shut_down()
        return False
