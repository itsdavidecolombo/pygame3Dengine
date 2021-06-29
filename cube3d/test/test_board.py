#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:04
# @Description: The unittest script for the game board class
#
#################################################
import unittest
from cube3d.board import GameBoard
from cube3d.data_model import Cube
from cube3d.test.loggertest import logger_mock
from cube3d.test.guardtest import guard_mock

class TestGameBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.guard = guard_mock.make_guard_mock()
        self.logger = logger_mock.make_logger_mock(self.guard)
        self.board  = GameBoard(Cube(), logger = self.logger)
        self.to_add = Cube()

    def tearDown(self) -> None:
        pass

    def test_game_board(self):
        self.assertTrue(self.board is not None)
        self.assertTrue(self.board.player is not None)
        self.assertTrue(len(self.board.creatures) == 0)

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
        board = GameBoard(player = Cube(), logger = self.logger, creatures = [self.to_add])
        self.assertTrue(len(board.creatures) == 1)

    def test_rotate_x(self):
        self.assertTrue(self.board.rotate_x())

    def test_rotate_y(self):
        self.assertTrue(self.board.rotate_y())

    def test_rotate_z(self):
        self.assertTrue(self.board.rotate_z())


if __name__ == '__main__':
    unittest.main()
