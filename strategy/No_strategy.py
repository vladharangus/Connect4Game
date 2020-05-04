from Board.cellconnect import Cell
from strategy.Strategy import Strategy
import random


class NoStrategy(Strategy):
    def drop(self, board, value):
        '''
        :param board: The game board
        :param value: 1 for the cpu
        :return: The cell corresponding to cpu's move
        '''
        empty = board.get_empty_cells()
        if len(empty) == 0:
            return None
        index = random.randint(0, len(empty) - 1)
        line = board.get_lowest_pt(empty[0].column)
        coloumn = empty[0].column

        #_____Check whether cpu can make 4 on diagonals
        val = self.try_diagonals(board, value)
        if val is not None:
            line = val[0]
            coloumn = val[1]

        #_____Check whether cpu can make 4 on lines
        elif self.try_lines(board, value) is not None:
            val = self.try_lines(board, value)
            line = val[0]
            coloumn = val[1]

        #____Check whether cpu can make 4 on columns
        elif self.try_columns(board, value) is not None:
            val = self.try_columns(board, value)
            line = val[0]
            coloumn = val[1]

        #____If it can't win within the next move it tries to block the human if one can win within the next move
        elif self.try_block_lines(board) is not None:
            val = self.try_block_lines(board)
            line = val[0]
            coloumn = val[1]

        elif self.try_block_columns(board) is not None:
            val = self.try_block_columns(board)
            line = val[0]
            coloumn = val[1]

        elif self.try_block_diagonals(board) is not None:
            val = self.try_block_diagonals(board)
            line = val[0]
            coloumn = val[1]

        board.set_value(line, coloumn, value)
        return Cell(line, coloumn, value)
    def try_diagonals(self, board, value):
        '''
        Checks if cpu can win on diagonals
        :param board: board game
        :param value: 1
        :return: the line and the column or None if it can't win
        '''
        for i in range(3):
            for j in range(4):
                if board.get_value(i, j) == value and board.get_value(i + 1, j + 1) == value and board.get_value(i + 2, j  + 2) == value and board.get_value(i + 3, j + 3) == 0:
                    return i + 3, j + 3
                if board.get_value(i, j) == 0 and board.get_value(i + 1, j + 1) == value and board.get_value(i + 2, j + 2) == value and board.get_value(i + 3, j + 3) == value:
                    return i, j
                if board.get_value(i, j) == value and board.get_value(i + 1, j + 1) == 0 and board.get_value(i + 2, j + 2) == value and board.get_value(i + 3, j + 3) == value:
                    return i + 1, j + 1
                if board.get_value(i, j) == value and board.get_value(i + 1, j + 1) == value and board.get_value(i + 2, j + 2) == 0 and board.get_value( i + 3, j + 3) == value:
                    return i + 2, j + 2

        for i in range(3):
            for j in range(3, 7):
                if board.get_value(i, j) == value and board.get_value(i + 1, j - 1) == value and board.get_value(i + 2, j  - 2) == value and board.get_value(i + 3, j - 3) == 0:
                    return i + 3, j - 3
                if board.get_value(i, j) == 0 and board.get_value(i + 1, j - 1) == value and board.get_value(i + 2, j - 2) == value and board.get_value(i + 3, j - 3) == value:
                    return i, j
                if board.get_value(i, j) == value and board.get_value(i + 1, j - 1) == 0 and board.get_value(i + 2, j - 2) == value and board.get_value(i + 3, j - 3) == value:
                    return i + 1, j - 1
                if board.get_value(i, j) == value and board.get_value(i + 1, j - 1) == value and board.get_value(i + 2, j - 2) == 0 and board.get_value( i + 3, j - 3) == value:
                    return i + 2, j - 2
        return None

    def try_block_diagonals(self, board):
        '''
               Checks if the human can win on diagonals
               :param board: board game
               :param value: 1
               :return: the line and the column or None if cpu can't block him
               '''
        for i in range(3):
            for j in range(4):
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j + 1) == 2 and board.get_value(i + 2, j  + 2) == 2 and board.get_value(i + 3, j + 3) == 0:
                    return i + 3, j + 3
                if board.get_value(i, j) == 0 and board.get_value(i + 1, j + 1) == 2 and board.get_value(i + 2, j + 2) == 2 and board.get_value(i + 3, j + 3) == 2:
                    return i, j
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j + 1) == 0 and board.get_value(i + 2, j + 2) == 2 and board.get_value(i + 3, j + 3) == 2:
                    return i + 1, j + 1
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j + 1) == 2 and board.get_value(i + 2, j + 2) == 0 and board.get_value( i + 3, j + 3) == 2:
                    return i + 2, j + 2

        for i in range(3):
            for j in range(3, 7):
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j - 1) == 2 and board.get_value(i + 2, j  - 2) == 2 and board.get_value(i + 3, j - 3) == 0:
                    return i + 3, j - 3
                if board.get_value(i, j) == 0 and board.get_value(i + 1, j - 1) == 2 and board.get_value(i + 2, j - 2) == 2 and board.get_value(i + 3, j - 3) == 2:
                    return i, j
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j - 1) == 0 and board.get_value(i + 2, j - 2) == 2 and board.get_value(i + 3, j - 3) == 2:
                    return i + 1, j - 1
                if board.get_value(i, j) == 2 and board.get_value(i + 1, j - 1) == 2 and board.get_value(i + 2, j - 2) == 0 and board.get_value( i + 3, j - 3) == 2:
                    return i + 2, j - 2
        return None

    def try_lines(self, board, value):
        '''
        Checks if cpu can win on lines
        :param board: the game board
        :param value: 1
        :return:line and column or None if it can't win
        '''
        for i in range(6):
            for j in range(4):
                if board.get_value(i, j) == value and board.get_value(i, j + 1) == value and board.get_value(i, j  + 2) == value and board.get_value(i, j + 3) == 0:
                    return i, j + 3
                if board.get_value(i, j) == 0 and board.get_value(i, j + 1) == value and board.get_value(i, j  + 2) == value and board.get_value(i, j + 3) == value:
                    return i, j
                if board.get_value(i, j) == value and board.get_value(i, j + 1) == 0 and board.get_value(i, j  + 2) == value and board.get_value(i, j + 3) == value:
                    return i, j + 1
                if board.get_value(i, j) == value and board.get_value(i, j + 1) == value and board.get_value(i, j  + 2) == 0 and board.get_value(i, j + 3) == value:
                    return i, j + 2
        return None

    def try_block_lines(self, board):
        '''
                       Checks if the human can win on lines
                       :param board: board game
                       :param value: 1
                       :return: the line and the column or None if cpu can't block him
                       '''
        for i in range(6):
            for j in range(4):
                if board.get_value(i, j) == 2 and board.get_value(i, j + 1) == 2 and board.get_value(i, j  + 2) == 2 and board.get_value(i, j + 3) == 0:
                    return i, j + 3
                if board.get_value(i, j) == 0 and board.get_value(i, j + 1) == 2 and board.get_value(i, j  + 2) == 2 and board.get_value(i, j + 3) == 2:
                    return i, j
                if board.get_value(i, j) == 2 and board.get_value(i, j + 1) == 0 and board.get_value(i, j  + 2) == 2 and board.get_value(i, j + 3) == 2:
                    return i, j + 1
                if board.get_value(i, j) == 2 and board.get_value(i, j + 1) == 2 and board.get_value(i, j  + 2) == 0 and board.get_value(i, j + 3) == 2:
                    return i, j + 2
        return None


    def try_columns(self, board, value):
        '''
                Checks if cpu can win on columns
                :param board: the game board
                :param value: 1
                :return:line and column or None if it can't win
                '''
        for i in range(3):
            for j in range(7):
                if board.get_value(i, j) == 0 and board.get_value(i + 1, j) == value and board.get_value(i + 2, j) == value and board.get_value(i + 3, j) == value:
                    return i, j
        return None

    def try_block_columns(self, board):
        '''
                       Checks if the human can win on columns
                       :param board: board game
                       :param value: 1
                       :return: the line and the column or None if cpu can't block him
                       '''
        for i in range(3):
            for j in range(7):
                if board.get_value(i, j) == 0 and board.get_value(i + 1, j) == 2 and board.get_value(i + 2, j) == 2 and board.get_value(i + 3, j) == 2:
                    return i, j
        return None