#################################################
#
# @Author: davidecolombo
# @Date: dom, 27-06-2021, 19:04
# @Description: The unittest script for the game board class
#
#################################################
import unittest
from cube3d.test.boardtest import board_mock

class TestGameBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.board = board_mock.make_board_mock(player = object(), logger = object(), creatures = None)

    def tearDown(self) -> None:
        pass

    def test_game_board(self):
        self.assertTrue(self.board.player is not None)
        self.assertTrue(len(self.board.creatures) == 0)
        self.assertTrue(self.board.logger is not None)

    def test_should_raise_ValueError_if_none_objects_in_constructor(self):
        try:
            board_mock.make_board_mock(player = None, logger = object(), creatures = None)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

        try:
            board_mock.make_board_mock(player = object(), logger = None, creatures = None)
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

        try:
            test_obj = object()
            board_mock.make_board_mock(player = object(), logger = object(), creatures = [test_obj, test_obj])
            self.fail()
        except ValueError as ex:
            print(ex.__str__())

    def test_add_creature(self):
        debug_msg = self.board.add_creature(object())
        self.assertTrue(debug_msg == 'Add creature ')
        self.assertTrue(len(self.board.creatures) == 1)

    def test_should_return_false_when_added_twice(self):
        test_object = object()
        debug_msg = self.board.add_creature(test_object)
        self.assertTrue(debug_msg == 'Add creature ')
        debug_msg = self.board.add_creature(test_object)
        self.assertTrue(debug_msg == 'Warning: not added because already exist')

    def test_remove_creature(self):
        test_object = object()
        debug_msg = self.board.add_creature(test_object)
        self.assertTrue(debug_msg == 'Add creature ')
        debug_msg = self.board.remove_creature(test_object)
        self.assertTrue(debug_msg == 'Remove creature ')
        self.assertTrue(len(self.board.creatures) == 0)

    def test_should_return_false_when_remove_not_found(self):
        debug_msg = self.board.remove_creature(object())
        self.assertTrue(debug_msg == 'Warning: not removed because not found')

    def test_creature_list_in_constructor(self):
        board = board_mock.make_board_mock(player = object(), logger = object, creatures = [object(), object()])
        self.assertTrue(len(board.creatures) == 2)


if __name__ == '__main__':
    unittest.main()
