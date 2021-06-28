#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:04
# @Description: The unittest script for the game board class
#
#################################################
import unittest
from cube3d.board import GameBoard
from cube3d.test.enginetest import engine_mock
from cube3d.data_model import Cube

def make_test_board():
    return GameBoard(engine = engine_mock.make_engine_mock())

class TestGameBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.board = make_test_board()
        self.to_add = Cube()

    def tearDown(self) -> None:
        pass

    def test_game_board(self):
        self.assertTrue(self.board is not None)

    def test_add_object(self):
        self.board.add_creature(self.to_add)
        self.assertTrue(len(self.board.creatures) == 1)

    def test_add_object_ValueError_add_twice(self):
        self.board.add_creature(self.to_add)
        try:
            self.board.add_creature(self.to_add)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_remove_object(self):
        self.board.add_creature(self.to_add)
        is_removed = self.board.remove_creature(self.to_add)
        self.assertTrue(len(self.board.creatures) == 0)
        self.assertTrue(is_removed)

    def test_remove_drawable_ValueError_element_not_present(self):
        try:
            self.board.remove_creature(self.to_add)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_live_objects_in_constructor(self):
        board = GameBoard(engine = engine_mock.make_engine_mock(), creatures = [self.to_add])
        self.assertTrue(len(board.creatures) == 1)

    def test_live_object_in_constructor_ValueError_duplicate(self):
        try:
            GameBoard(engine = engine_mock.make_engine_mock(), creatures = [self.to_add, self.to_add])
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_set_player(self):
        self.board.set_player(Cube())
        self.assertTrue(self.board.player is not None)

    def test_set_player_ValueError(self):
        self.board.set_player(Cube())
        try:
            self.board.set_player(Cube())
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_rotate_x(self):
        self.assertTrue(self.board.rotate_x() == 'rotate cube on x axis')

    def test_rotate_y(self):
        self.assertTrue(self.board.rotate_y() == 'rotate cube on y axis')

    def test_rotate_z(self):
        self.assertTrue(self.board.rotate_z() == 'rotate cube on z axis')


if __name__ == '__main__':
    unittest.main()
