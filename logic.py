from grid import Grid
from interface import Interface
from bot import easy_bot_move, hard_bot_move
from time import sleep


class Game:
    """
    A class to represent a Game.

    Attributes
    ----------
    player1 : str
        name of player1
    player2 : str
        name of player2
    interface : Interface
        window to represent a game
    grid : Grid
        grid of the game

    Methods
    -------
    run():
        creates interface
        creates a loop of game
    play(mode, size):
        sequence of taking moves and giving grid to interface
    """
    def __init__(self):
        """
        Initializes the players for the game
        """
        self.player1 = "C"
        self.player2 = "N"

    def run(self):
        """
        Initializes the interface and create a while loop of taking
        the settings, playing and showing the winner
        """
        self.interface = Interface()
        while True:
            mode = self.interface.choose_mode()
            size = self.interface.choose_size()
            winner = self.play(mode, size)
            self.interface.over(winner)

    def play(self, mode: str, size: int) -> str:
        """
        Sequence of taking and showing players decisions

        : param mode : has to be from ['2_players', '"AI-AI',
                                     'AI-Easy', 'AI-Hard']
        : type mode : str

        : param size : has to be odd and more than 5

        : type size : int
        """
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
            while True:
                self.interface.change_caption("Gracz Czerwony")
                cell = hard_bot_move(self.grid, self.player1, self.interface)
                self.grid.change_cell(cell, self.player1)
                self.interface.draw_board(self.interface.board)
                self.interface.check_for_closing()

                winner = self.grid.check_win()
                if winner is not None:
                    return winner

                cell = hard_bot_move(self.grid, self.player2, self.interface)
                self.grid.change_cell(cell, self.player2)
                self.interface.draw_board(self.interface.board)
                self.interface.check_for_closing()

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
