from grid import Grid
from interface import Interface
from bot import easy_bot_move, hard_bot_move
from time import sleep

class Game:
    def __init__(self):
        self.player1 = "C"
        self.player2 = "N"
        self.size = 13  # musi być nieparzyste
        self.grid = Grid(self.player1, self.player2, self.size)

    def check_near_connection(self,
                              point: tuple[int, int],
                              player: str,
                              check_grid=None) -> list:

        row, column = point
        check_grid = self.grid.grid if check_grid is None else check_grid
        check_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        neighbors = [(row + x, column + y) for x, y in check_list
                     if (0 <= row + x <= self.size - 1 and
                         0 <= column + y <= self.size - 1 and
                         check_grid[row + x][column + y] == player)]
        return neighbors

    def check_win_connection(self,
                             player: str,
                             check_grid=None,
                             cords=None,
                             checked=None) -> bool:

        check_grid = self.grid.grid if check_grid is None else check_grid
        checked = checked if checked is not None else []

        if cords is None:
            row, column = 1, 0
            if player == self.player2:
                rotated = list(zip(*check_grid))[::-1]
                rotated = [list(elem) for elem in rotated]
                check_grid = rotated
        else:
            row, column = cords

        last_row_0 = row
        while True:
            args = (row, column), player, check_grid
            next_checks = self.check_near_connection(*args)
            if column == 0 and not next_checks:
                row += 2
                last_row_0 = row
                if row > self.size - 1:
                    return False

            elif column == 0 and len(next_checks) == 1:
                checked.append((row, column))
                row, column = next_checks[0]

            elif column != 0 and len(next_checks) == 1:
                if last_row_0 == self.size - 1:
                    return False
                else:
                    last_row_0 += 2
                    row, column = last_row_0, 0

            elif column != 0 and len(next_checks) == 2:
                checked.append((row, column))
                if next_checks[0] not in checked:
                    row, column = next_checks[0]
                elif next_checks[1] not in checked:
                    row, column = next_checks[1]
                else:
                    if last_row_0 == self.size - 1:
                        return False
                    else:
                        last_row_0 += 2
                        row, column = last_row_0, 0

            elif column != 0 and (3 <= len(next_checks) <= 4):
                checked.append((row, column))
                for check in next_checks:
                    if check not in checked:
                        if self.check_win_connection(player,
                                                     check_grid,
                                                     check,
                                                     checked):
                            return True
                        checked.append(check)
                else:
                    if last_row_0 == self.size - 1:
                        return False
                    else:
                        last_row_0 += 2
                        row, column = last_row_0, 0

            else:
                if last_row_0 == self.size - 1:
                    return False
                else:
                    last_row_0 += 2
                    row, column = last_row_0, 0

            if column >= self.size - 1:
                return True

    def check_win(self) -> str | None:
        if self.check_win_connection(self.player1):
            return self.player1
        elif self.check_win_connection(self.player2):
            return self.player2
        return None

    def run(self):
        self.interface = Interface(self.grid)
        while True:
            mode = self.interface.choose_mode()
            winner = self.play(mode)
            self.interface.over(winner)

    def play(self, mode):
        self.grid.clear_grid()
        self.interface.clear_screen()
        self.interface.draw_board(self.interface.board)

        if mode == "2_players":
            moves = 0
            while self.check_win() is None:
                cell = self.interface.get_click()
                player = self.player1 if moves % 2 == 0 else self.player2
                self.grid.change_cell(cell, player)
                self.interface.draw_board(self.interface.board)
                moves += 1
            return self.check_win()

        # elif mode == "test":
        #     moves = 0
        #     while self.check_win() is None:
        #         cell = easy_bot_move(self.grid)
        #         player = self.player1 if moves % 2 == 0 else self.player2
        #         self.grid.change_cell(cell, player)
        #         self.interface.draw_board(self.interface.board)
        #         moves += 1
        #         sleep(0.333)
        #     return self.check_win()

        else:
            while True:
                cell = self.interface.get_click()
                self.grid.change_cell(cell, self.player1)
                self.interface.draw_board(self.interface.board)

                winner = self.check_win()
                if winner is not None:
                    return winner

                if mode == "AI-Easy":
                    cell = easy_bot_move(self.grid)
                elif mode == "AI-Hard":
                     cell = hard_bot_move(self.grid)

                self.grid.change_cell(cell, self.player2)
                sleep(0.5)
                self.interface.draw_board(self.interface.board)
                winner = self.check_win()
                if winner is not None:
                    return winner
