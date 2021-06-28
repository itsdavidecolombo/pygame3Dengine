#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:05
# @Description: the Game board class for controlling the movement of the player and other objects within the scene
#
#################################################

class GameBoard:

    def __init__(self, engine, player = None, creatures: list = None):
        self.engine = engine
        self.player = player
        self.creatures = _init_list(creatures)

    def set_player(self, player) -> bool:
        if self.player is not None:
            # TODO log warning message
            return False
        self.player = player
        return True

    def add_creature(self, to_add) -> bool or ValueError:
        for c in self.creatures:
            if c == to_add:
                # TODO log warning message
                return False
        self.creatures.append(to_add)
        return True

    def remove_creature(self, to_remove) -> bool:
        for c in self.creatures:
            if c == to_remove:
                self.creatures.remove(to_remove)
                return True
        # TODO log warning message
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
            print('Cannot find reference to the player object')
            return False
        return True

# ========================= MODULE FUNCTIONS =========================
def _init_list(a_list):
    if a_list is None:
        return []

    set_of_el = set()
    for el in a_list:
        if el in set_of_el:
            raise ValueError(f'Error during list initialization: list contains duplicates')
        else:
            set_of_el.add(el)
    return a_list
