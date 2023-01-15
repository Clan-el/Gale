from grid import Grid
from interface import Interface
from bot import easy_bot_move, hard_bot_move
from time import sleep


class Game:
    def __init__(self):
        self.player1 = "C"
        self.player2 = "N"

    def run(self):
        self.interface = Interface()
        while True:
            mode = self.interface.choose_mode()
            size = self.interface.choose_size()
            winner = self.play(mode, size)
            self.interface.over(winner)

    def play(self, mode, size):
        self.grid = Grid(self.player1, self.player2, size)
        self.interface.set_grid(self.grid)
        self.interface.clear_screen()
        self.interface.draw_board(self.interface.board)

        if mode == "2_players":
            moves = 0
            while self.grid.check_win() is None:
                txt = "Gracz Czerwony" if moves % 2 == 0 else "Gracz Niebieski"
                self.interface.change_caption(txt)
                cell = self.interface.get_click()
                player = self.player1 if moves % 2 == 0 else self.player2
                self.grid.change_cell(cell, player)
                self.interface.draw_board(self.interface.board)
                moves += 1
            return self.grid.check_win()

        elif mode == "AI-AI":
            self.grid.move = 0
            while True:
                self.grid.move += 1
                self.interface.change_caption("Gracz Czerwony")
                cell = hard_bot_move(self.grid, self.player1, self.interface)
                self.grid.change_cell(cell, self.player1)
                self.interface.draw_board(self.interface.board)

                winner = self.grid.check_win()
                if winner is not None:
                    return winner

                cell = hard_bot_move(self.grid, self.player2, self.interface)
                self.grid.change_cell(cell, self.player2)
                self.interface.draw_board(self.interface.board)

                winner = self.grid.check_win()
                if winner is not None:
                    return winner

        else:
            while True:
                self.interface.change_caption("Gracz Czerwony")
                cell = self.interface.get_click()
                self.grid.change_cell(cell, self.player1)
                self.interface.draw_board(self.interface.board)

                winner = self.grid.check_win()
                if winner is not None:
                    return winner

                if mode == "AI-Easy":
                    text = "Gracz Niebieski zastanawia się"
                    self.interface.change_caption(text)
                    sleep(0.7)
                    cell = easy_bot_move(self.grid)
                elif mode == "AI-Hard":
                    args = self.grid, self.player2, self.interface
                    cell = hard_bot_move(*args)

                self.grid.change_cell(cell, self.player2)
                self.interface.draw_board(self.interface.board)
                winner = self.grid.check_win()
                if winner is not None:
                    return winner
