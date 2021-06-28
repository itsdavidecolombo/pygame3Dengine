#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 15:57
# @Description: Event Handler class for handling pygame event during game loop
#
#################################################
import pygame
from cube3d.board import GameBoard

class EventHandler:

    def __init__(self, game_engine, board: GameBoard):
        self.engine = game_engine
        self.board  = board

    def handle_events(self) -> bool:
        for event in pygame.event.get():
            # QUIT EVENT
            if event.type == pygame.QUIT:
                self.__quit_engine()

            # KEYDOWN EVENTS
            if event.type == pygame.KEYDOWN:
                self.__handle_keydown(event)

            # KEYUP EVENTS
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_j:
                    pass

        return True

# ============================= HANDLE KEYDOWN METHOD =============================
    def __handle_keydown(self, event):
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
        self.engine.stop()
        return False
