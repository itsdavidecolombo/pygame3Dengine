#################################################
#
# @Author: davidecolombo
# @Date: mar, 29-06-2021, 16:08
# @Description: A mock class for the game board
#
#################################################
from cube3d.board import GameBoard

def make_board_mock(player, logger):
    return BoardMock(player = player, logger = logger)

class BoardMock(GameBoard):

    def __init__(self, player, logger):
        super().__init__(player = player, logger = logger)

    def add_creature(self, to_add) -> str:
        debug = ''
        for c in self.creatures:
            if c == to_add:
                debug += 'Warning: not added because already exist'
                return debug
        debug += 'Add creature '
        self.creatures.append(to_add)
        return debug

    def remove_creature(self, to_remove) -> str:
        debug = ''
        for c in self.creatures:
            if c == to_remove:
                debug += 'Remove creature '
                self.creatures.remove(to_remove)
                return debug
        debug += 'Warning: not removed because not found'
        return debug

    def rotate_x(self) -> str:
        return 'Rotating on x axis'

    def rotate_y(self):
        return 'Rotating on y axis'

    def rotate_z(self):
        return 'Rotating on z axis'
