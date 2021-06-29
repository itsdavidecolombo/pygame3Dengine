#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:05
# @Description: the Game board class for controlling the movement of the player and other objects within the scene
#
#################################################
from cube3d.logger import Logger, LoggerLevel

class GameBoard:

    def __init__(self, player, logger: Logger, creatures: list = None):
        self.logger = logger
        self.__safe_init_player(player)
        self.creatures = self.__safe_init_list(creatures)

    def __safe_init_player(self, player):
        if player is None:
            self.logger.log(level = LoggerLevel.Severe, msg = 'GameBoard: player is None...')
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: setting the player...')
        self.player = player

    def __safe_init_list(self, creatures):
        if creatures is None:
            return []

        set_of_el = set()
        for c in creatures:
            if c in set_of_el:
                self.logger.log(level = LoggerLevel.Severe, msg = 'GameBoard: creature list contains duplicates...')
            else:
                set_of_el.add(c)
        return creatures

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

    def rotate_x(self) -> bool:
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: rotate cube around x axis...')
        return True

    def rotate_y(self) -> bool:
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: rotate cube around y axis...')
        return True

    def rotate_z(self) -> bool:
        self.logger.log(level = LoggerLevel.Debug, msg = 'GameBoard: rotate cube around z axis...')
        return True
