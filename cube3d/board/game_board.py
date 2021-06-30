#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:05
# @Description: the Game board class for controlling the movement of the player and other objects within the scene
#
#################################################
from cube3d.logger import Logger, LoggerLevel

class GameBoard:

    def __init__(self, player, logger: Logger):
        self.logger = self.__safe_init_logger(logger)
        self.player = self.__safe_init_player(player)
        self.creatures = []

    def __safe_init_player(self, player):
        if player is None:
            raise ValueError('GameBoard: player is None...')
        return player

    def __safe_init_logger(self, logger):
        if logger is None:
            raise ValueError('GameBoard: cannot start the game without a valid logger...')
        return logger

# =================================== OTHER METHODS ===================================
    def add_creature(self, to_add) -> bool:
        for c in self.creatures:
            if c == to_add:
                self.logger.log(level = LoggerLevel.Warning, msg = 'GameBoard: creature not added because already exist...')
                return False
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: add creature...')
        self.creatures.append(to_add)
        return True

    def remove_creature(self, to_remove) -> bool:
        for c in self.creatures:
            if c == to_remove:
                self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: remove creature...')
                self.creatures.remove(to_remove)
                return True
        self.logger.log(level = LoggerLevel.Warning, msg = 'GameBoard: creature not removed because not found...')
        return False

    def rotate_x(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: rotate cube around x axis...')

    def rotate_y(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: rotate cube around y axis...')

    def rotate_z(self):
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: rotate cube around z axis...')


    # TODO add draw method that cycles through the objects and draws everyone
