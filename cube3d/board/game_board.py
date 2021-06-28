#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:05
# @Description: the Game board class for controlling the movement of the player and other objects within the scene
#
#################################################

class GameBoard:

    def __init__(self, engine, creatures: list = None):
        self.engine = engine
        self.creatures = _init_list(creatures)

    def add_creature(self, to_add) -> bool or ValueError:
        for c in self.creatures:
            if c == to_add:
                raise ValueError(f'Cannot add the same object twice')
        self.creatures.append(to_add)
        return True

    def remove_creature(self, to_remove) -> bool or ValueError:
        self.creatures.remove(to_remove)
        return True

    # def jump(self):
    #     pass
    #
    # def fall(self):
    #     pass
    #
    # def move_left(self):
    #     pass
    #
    # def move_right(self):
    #     pass


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
