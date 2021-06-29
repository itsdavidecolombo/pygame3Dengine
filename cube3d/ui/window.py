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

    def __init__(self, logger: Logger, title: str = '', width: int = DEFAULT_WIDTH, height: int = DEFAULT_HEIGHT):
        self.title = title
        self.width, self.height = self.__safe_init_dimensions(width, height)
        self.logger = self.__safe_init_logger(logger)
        self.__DISPLAY = None
        self.__is_opened = False

    def __safe_init_logger(self, logger: Logger) -> Logger:
        if logger is None:
            raise ValueError('Window: logger is None...')
        return logger

    def __safe_init_dimensions(self, width: int, height: int) -> (int, int):
        if width <= 0:
            raise ValueError(f'Window: width {width} is invalid...')
        if height <= 0:
            raise ValueError(f'Window: height {height} is invalid...')
        return width, height

    def set_size(self, width, height) -> None:
        self.width, self.height = self.__safe_init_dimensions(width, height)

    def set_title(self, title: str) -> None:
        self.title = title

    def is_opened(self):
        return self.__is_opened

    def open(self) -> pygame.Surface:
        if self.__is_opened:
            self.logger.log(level = LoggerLevel.Severe, msg = 'Window: already opened...')
        pygame.init()
        self.__DISPLAY = pygame.display.set_mode(size = (self.width, self.height))
        pygame.display.set_caption(self.title)
        self.__is_opened = True
        return self.__DISPLAY

    def close(self) -> None:
        if not self.__is_opened:
            self.logger.log(level = LoggerLevel.Severe, msg = 'Window: not open...')
        self.__is_opened = False
        pygame.quit()
