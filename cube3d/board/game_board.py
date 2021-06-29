#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:05
# @Description: the Game board class for controlling the movement of the player and other objects within the scene
#
#################################################
import logging

class GameBoard:

    def __init__(self, player, creatures: list = None):
        self.player = player
        self.creatures = _init_list(creatures)

    def add_creature(self, to_add) -> bool:
        for c in self.creatures:
            if c == to_add:
                logging.log(level = logging.WARNING, msg = f'Cannot add creature: already exist')
                return False
        self.creatures.append(to_add)
        return True

    def remove_creature(self, to_remove) -> bool:
        for c in self.creatures:
            if c == to_remove:
                self.creatures.remove(to_remove)
                return True
        logging.log(level = logging.WARNING, msg = f'Cannot remove creature: not found')
        return False

    def rotate_x(self) -> bool:
        if not self.__check_before_rotate():
            return False
        print('rotate cube around x axis')
        return True

    def rotate_y(self) -> bool:
        if not self.__check_before_rotate():
            return False
        print('rotate cube around y axis')
        return True

    def rotate_z(self) -> bool:
        if not self.__check_before_rotate():
            return False
        print('rotate cube around z axis')
        return True

    def __check_before_rotate(self) -> bool:
        if self.player is None:
            logging.log(level = logging.WARNING, msg = f'Cannot set player: player is not None')
            return False
        return True

# ========================= MODULE FUNCTIONS =========================
def _init_list(a_list):
    if a_list is None:
        return []

    set_of_el = set()
    for el in a_list:
        if el in set_of_el:
            logging.log(level = logging.ERROR, msg = f'Error during list initialization: list contains duplicates')
            raise ValueError(f'Error during list initialization: list contains duplicates')
        else:
            set_of_el.add(el)
    return a_list
