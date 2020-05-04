import numpy as np
from texttable import Texttable
from Board.cellconnect import Cell


class Board:
    def __init__(self, empty_value = 0):
        self.__empty_value = empty_value
        self.__cells = self.__create_board()

    def __create_board(self): #creates the board
        '''
        :return: The board
        '''
        board = np.zeros((6, 7))
        return  board

    def check_diagonals(self, value):
        '''
        This function checks if there are 4 consecutive cells with the same value on diagonals
        :param value: the value
        :return: True if there are 4 cons cells of the same value, False, otherwise
        '''
        for i in range(3):
            for j in range(4):
                if self.__cells[i][j] == value and self.__cells[i + 1][j + 1] == value and self.__cells[i + 2][j + 2] == value and self.__cells[i + 3][j + 3] == value:
                    return True

        for i in range(3):
            for j in range(3, 7):
                if self.__cells[i][j] == value and self.__cells[i + 1][j - 1] == value and self.__cells[i + 2][j - 2] == value and self.__cells[i + 3][j - 3] == value:
                    return True
        return False

    def __str__(self):
        res = Texttable()
        for line in self.__cells:
            s = " ".join([str(int(value)) for value in line]) + "\n"
            res.add_row(s)
        return res.draw()

    def get_line_values(self, line):
        '''
        Returns the values of the cells on the given line
        :param line: the number of line
        :return: All the values on that line
        '''
        return self.__cells[line]

    def get_column_values(self, column):
        '''
        Returns the values of the cells on the given line
        :param line: the number of column
        :return: A list containing the values for each cell in that column
        '''
        return [int(self.__cells[i][column]) for i in range(6)]

    def get_value(self, line, column):
        '''
        This function returns the value of a certen cell
        :param line: the number of line
        :param column: the number of column
        :return: the value of the cell
        '''
        return int(self.__cells[line][column])

    def set_value(self, line, column, value):
        '''
        This function sets the value of a certen cell
        :param line: the number of line
        :param column: the number of column
        :return: the value to be given
        '''
        self.__cells[line][column] = value

    def get_empty_cells(self):
        '''
        :return: A list of empty cells
        '''
        return [cell for cell in self.get_all_cells()
                if cell.value == self.__empty_value]

    def get_all_cells(self):
        res = []
        for i in range(6):
            for j in range(7):
                res.append(Cell(i, j, self.__cells[i][j]))
        return res

    def get_cell_values(self):
        return self.__cells

    def get_lowest_pt(self, coloumn):
        '''
        This function returns the lowest cell in the given column which is empty
        :param coloumn: the number of column
        :return: The corresponding line
        '''
        for i in range(5, -1, -1):
            if self.get_value(i, coloumn) == 0:
                return i
        return -1

