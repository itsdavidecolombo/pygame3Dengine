#################################################
#
# @Author: davidecolombo
# @Date: sab, 26-06-2021, 19:08
# @Description: The Window class
#
#################################################
import pygame
from typing import ClassVar
from cube3d.logger import Logger, LoggerLevel

class Window:
    DEFAULT_WIDTH:  ClassVar[int] = 800
    DEFAULT_HEIGHT: ClassVar[int] = 600

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self, logger: Logger, title: str = None, width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):
        self.title     = title
        self.width     = width
        self.height    = height
        self.logger    = logger
        self.__DISPLAY = None
        self.__is_opened = False

    def set_size(self, width, height):
        self.width  = width
        self.height = height

    def set_title(self, title):
        self.title = title

    def is_opened(self):
        return self.__is_opened

    def open(self) -> pygame.Surface:
        if self.__is_opened:
            self.logger.log(level = LoggerLevel.Severe, msg = 'Window: already opened')
        self.__DISPLAY = pygame.display.set_mode(size = (self.width, self.height))
        pygame.display.set_caption(self.title)
        self.__is_opened = True
        return self.__DISPLAY

    def close(self) -> None:
        if not self.__is_opened:
            self.logger.log(level = LoggerLevel.Severe, msg = 'Window: not open')
        pygame.quit()
        self.__is_opened = False
