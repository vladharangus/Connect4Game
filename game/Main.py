import tkinter

from Board.board import Board
from game.Game import Game
from gui.Gui import Gui
from gui.GuiGame import guigame
from player.Computer import Computer
from player.Human import Human
from strategy.No_strategy import NoStrategy

board = Board()
strategy = NoStrategy()
player1 = Computer("1", board, strategy)
player2 = Human("2", board)
game = Game(board, player1, player2)

game.play()

print("bye")
# board = Board()
# strategy = NoStrategy()
# player1 = Computer("1", board, strategy)
# player2 = Human("2", board)
# game = guigame(player2, player1, board)
# root = tkinter.Tk()
# my_gui = Gui(root, game)
# root.mainloop()