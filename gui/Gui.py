import tkinter
from tkinter import Button
class Gui:
    def __init__(self, master, game):
        self.master = master
        self.game = game
        master.title("Connect4")
        self.start()

    def start(self):
        lines = 6
        columns = 7
        self.buttons = []
        for line in range(lines):
            button_row = []
            for column in range(columns):
                button = Button(self.master, text = " ", bg = 'green', command = lambda x = line, y = column: self.send_parameters(x, y))
                button.grid(row = line, column = column)
                button_row.append(button)
            self.buttons.append(button_row)

    def send_parameters(self, x, y):
        lst1 = self.game.player_move(self.game.p1, x, y)
        game_status = self.game.game_over(self.game.last_drop)
        winner = self.game.winner()
        if winner or game_status:
            self.finish_frame(winner, game_status)
        lst2 = self.game.computer_move(self.game.p2, x, y)
        game_status = self.game.game_over(self.game.last_drop)
        winner = self.game.winner()
        if winner or game_status:
            self.finish_frame(winner, game_status)
        else:
            self.buttons[lst1.line][lst1.column]["bg"] = "red"
            self.buttons[lst2.column][lst2.column]["bg"] = "yellow"

    def finish_frame(self, winner, game_statues):
        self.master.destroy()
        window = tkinter.Tk()
        window.title("Game over")
        if winner is True:
            if self.game.last_drop.value == 2:
                text = "You won"
            else:
                text = "Computer won"
        else:
            text = "Draw"
        label = tkinter.Label(window, text = text)
        label.grid()
        window.mainloop()
