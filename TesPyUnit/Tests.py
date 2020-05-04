import unittest

from Board.board import Board


class Test_Board(unittest.TestCase):
    def setUp(self):
        self.__board = Board()

    def test_get_column_values(self):
        self.__board.set_value(0, 0, 1)
        values = self.__board.get_column_values(0)
        self.assertEqual(values[0], 1)

    def test_get_line_values(self):
        self.__board.set_value(0, 0, 1)
        values = self.__board.get_line_values(0)
        self.assertEqual(values[0], 1)

    def test_get_value(self):
        self.__board.set_value(0, 0, 1)
        value = self.__board.get_value(0, 0)
        self.assertEqual(value, 1)

    def test_set_value(self):
        self.__board.set_value(0, 0, 4)
        value = self.__board.get_value(0, 0)
        self.assertEqual(value, 4)

    def test_get_all_cells(self):
        lst = self.__board.get_all_cells()
        self.assertEqual(len(lst), 42)

    def test_get_empty_cells(self):
        self.__board.set_value(0, 0, 1)
        lst = self.__board.get_empty_cells()
        self.assertEqual(len(lst), 41)

    def test_get_lowest_point(self):
        self.__board.set_value(5, 0, 1)
        line = self.__board.get_lowest_pt(0)
        self.assertEqual(line, 4)

    def test_check_diagonals(self):
        self.assertEqual(self.__board.check_diagonals(1), False)

    def test_get_cells_values(self):
        self.__board.set_value(0, 0, 4)
        lst = self.__board.get_cell_values()
        self.assertEqual(lst[0][0], 4)


if __name__ == '__main__':
    unittest.main()
