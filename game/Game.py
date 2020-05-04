from player.Human import Human


class Game:
    def __init__(self, board, player1, player2):
        self.__board = board
        self.__player1 = player1
        self.__player2 = player2

        self.__last_drop = None

    def play(self):
        while True:
            if self.__drop(self.__player1, 1):
                break

            if self.__drop(self.__player2, 2):
                break

    def __read_cmd(self):
        try:
            coloumn = int(input("Insert the column "))
            coloumn = coloumn -1
            line = self.__board.get_lowest_pt(coloumn)
            return line, coloumn
        except ValueError:
            print("Invalid data has been introduced")
        except IndexError:
            print("Index out of range")

    def __draw_board(self):
        print(self.__board)

    def __drop(self, player, value):

        line, coloumn = -1, -1
        if type(player) is Human:
            self.__draw_board()
            try:
                line, coloumn = self.__read_cmd()
            except TypeError:
                print("Invalid data has been introduced")
                return True

        #self.__last_drop = player.drop(line, coloumn, value)
        self.__last_drop = player.drop(line, coloumn, value)
        winner = self.__winner()
        if self.__game_over(self.__last_drop) or winner:
            self.__show_game_status()
            return True
        return False

    def __show_game_status(self):
        print("game over")
        if self.__last_drop.value == 1:
            print("CPU won")
        else:
            print("You won")
        self.__draw_board()

    def __game_over(self, cell):
        if cell is None:
            return True
        if len(self.__board.get_empty_cells()) == 0:
            return True
        return False

    def __winner(self):
        line = self.__last_drop.line
        column = self.__last_drop.column
        value = self.__last_drop.value
        # check lines
        line_values = self.__board.get_line_values(line)
        if self.__check_values(line_values, value):
            return True

        # check columns
        column_values = self.__board.get_column_values(column)
        if self.__check_values(column_values, value):

            return True

        return self.__board.check_diagonals(value)

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



