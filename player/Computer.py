from player.Player import Player


class Computer(Player):
    def __init__(self, name, board, strategy):
        super().__init__(name, board)
        self.__strategy = strategy
    def drop(self, line, coloumn, value):
        '''
                Returns a cell modified according to cpu's move
                :param line: the number of line
                :param column: the number of column
                :param value: the value..1
                :return: A cell
                '''
        return self.__strategy.drop(self._board, value)


