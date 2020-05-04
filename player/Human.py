from Board.cellconnect import Cell
from player.Player import Player


class Human(Player):
    def drop(self, line, column, value):
        '''
        Returns a cell modified according to human's move
        :param line: the number of line
        :param column: the number of column
        :param value: the value..2
        :return: A cell
        '''
        self._board.set_value(line, column,  value)
        return Cell(line, column, value)