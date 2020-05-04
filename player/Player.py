from abc import abstractmethod

from Board.cellconnect import Cell


class Player:
    def __init__(self, name, board):
        self.__name = name
        self._board = board

    @abstractmethod
    def drop(self, *args) -> Cell:
        pass