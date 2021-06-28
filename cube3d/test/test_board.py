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
        self.board  = make_test_board()
        self.to_add = Cube()

    def tearDown(self) -> None:
        pass

    def test_game_board(self):
        self.assertTrue(self.board is not None)
        self.assertTrue(self.board.engine is not None)
        self.assertTrue(self.board.player is None)

    def test_add_creature(self):
        self.board.add_creature(self.to_add)
        self.assertTrue(len(self.board.creatures) == 1)

    def test_should_return_false_when_added_twice(self):
        is_set = self.board.add_creature(self.to_add)
        self.assertTrue(is_set)
        is_set = self.board.add_creature(self.to_add)
        self.assertFalse(is_set)

    def test_remove_creature(self):
        self.board.add_creature(self.to_add)
        is_removed = self.board.remove_creature(self.to_add)
        self.assertTrue(is_removed)
        self.assertTrue(len(self.board.creatures) == 0)

    def test_should_return_false_when_remove_not_found(self):
        is_removed = self.board.remove_creature(self.to_add)
        self.assertFalse(is_removed)

    def test_creature_list_in_constructor(self):
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

    def test_shoudl_return_false_when_player_already_set(self):
        is_set = self.board.set_player(Cube())
        self.assertTrue(is_set)
        is_set = self.board.set_player(Cube())
        self.assertFalse(is_set)

    def test_rotate_x(self):
        self.assertFalse(self.board.rotate_x())
        self.board.set_player(Cube())
        self.assertTrue(self.board.rotate_x())

    def test_rotate_y(self):
        self.assertFalse(self.board.rotate_y())
        self.board.set_player(Cube())
        self.assertTrue(self.board.rotate_y())

    def test_rotate_z(self):
        self.assertFalse(self.board.rotate_z())
        self.board.set_player(Cube())
        self.assertTrue(self.board.rotate_z())


if __name__ == '__main__':
    unittest.main()
