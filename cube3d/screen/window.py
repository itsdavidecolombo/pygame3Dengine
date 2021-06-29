#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:08
# @Description: The Window class
#
#################################################
import pygame
from typing import ClassVar
import logging

class Window:
    _DEFAULT_WIDTH:  ClassVar[int] = 800
    _DEFAULT_HEIGHT: ClassVar[int] = 600

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, title: str = None, width: int = _DEFAULT_WIDTH, height: int = _DEFAULT_HEIGHT):
        self.title     = title
        self.width     = width
        self.height    = height
        self.__DISPLAY = None
        self.__is_opened = False

    def set_size(self, width, height):
        self.width  = width
        self.height = height

    def set_title(self, title):
        self.title = title

    def is_opened(self):
        return self.__is_opened

    def open(self) -> ValueError or pygame.Surface:
        if self.__is_opened:
            logging.error(msg = f'Window is already opened')
            raise ValueError(f'Window is already opened')
        self.__DISPLAY = pygame.display.set_mode(size = (self.width, self.height))
        pygame.display.set_caption(self.title)
        self.__is_opened = True
        return self.__DISPLAY

    def close(self) -> bool:
        if not self.__is_opened:
            logging.error(msg = f'Window is not open')
            raise ValueError(f'Window is not open')
        pygame.quit()
        self.__is_opened = False
        return True
