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
                self.engine.stop()
                return False

            # KEYDOWN EVENTS
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.engine.move_right()
                if event.key == pygame.K_q:
                    self.engine.move_left()
                if event.key == pygame.K_j:
                    self.engine.jump()
                if event.key == pygame.K_ESCAPE:
                    self.engine.stop()
                    return False

            # KEYUP EVENTS
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_j:
                    self.engine.fall()

        return True
