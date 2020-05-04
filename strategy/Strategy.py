from abc import abstractmethod

from Board.cellconnect import Cell


class Strategy:
    @abstractmethod
    def drop(self, *args) -> Cell:
        pass