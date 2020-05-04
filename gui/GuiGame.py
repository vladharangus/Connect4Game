class guigame:
    def __init__(self, p1, p2, board):
        self.p1 = p1
        self.p2 = p2
        self.board = board
        self.last_drop = None

    def player_move(self, player, x, y):
        lst = player.drop(x, y, 2)
        self.last_drop = lst
        return lst

    def computer_move(self, player, x, y):
        if self.last_drop.value == 2:
            lst = player.drop(x, y, 1)
            self.last_drop = lst
            return lst

    def winner(self):
        line = self.last_drop.line
        column = self.last_drop.column
        value = self.last_drop.value
        # check lines
        line_values = self.board.get_line_values(line)
        if self.__check_values(line_values, value):
            return True

        # check columns
        column_values = self.board.get_column_values(column)
        if self.__check_values(column_values, value):
            return True

        return self.board.check_diagonals(value)

    def __check_values(self, line_values, value):
        cont  = 0
        for x in line_values:
            if x == value:
                cont = cont + 1 #daca am gasit o valoare egala pe pozitie consecutiva incrementez contorul
            else:# daca am gasit valoare diferita verific valoarea contorului si il setez la 0
                if cont == 4:
                    return True
                cont = 0
        if cont == 4:
            return True
        return False

    def game_over(self, cell):
        if cell is None:
            return True
        if len(self.board.get_empty_cells()) == 0:
            return True
        return False