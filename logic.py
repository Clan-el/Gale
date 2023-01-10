from grid import grid
from copy import deepcopy


class Game:
    def __init__(self, game_grid=None):
        if game_grid is None:
            self._grid = deepcopy(grid)
        else:
            self._grid = deepcopy(game_grid)

        self.player1 = "C"
        self.player2 = "N"

    def clear_grid(self):
        self._grid = deepcopy(grid)

    def get_grid(self) -> list[list[str | None]]:
        return self._grid

    def get_cell(self, point: tuple[int, int]) -> str | None:
        return self._grid[point[0]][point[1]]

    def change_cell(self, point: tuple[int, int], player: str):
        i, j = point
        self._grid[i][j] = player

    def check_near_connection(self,
                              point: tuple[int, int],
                              player: str,
                              check_grid=None) -> list:

        i, j = point
        check_grid = self._grid[:] if check_grid is None else check_grid
        check_list = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        neighbors = [(i + x, j + y) for x, y in check_list
                     if (0 <= i + x <= 12 and 0 <= j + y <= 12 and
                     check_grid[i + x][j + y] == player)]
        return neighbors

    def check_win_connection(self,
                             player: str,
                             check_grid=None,
                             cords=None,
                             checked=None) -> bool:

        check_grid = deepcopy(self._grid) if check_grid is None else check_grid
        checked = checked if checked is not None else []

        if cords is None:
            i, j = 1, 0
            if player == self.player2:
                rotated = list(zip(*check_grid))[::-1]
                rotated = [list(elem) for elem in rotated]
                check_grid = rotated
        else:
            i, j = cords

        last_i_0 = i
        while True:
            args = (i, j), player, check_grid
            next_checks = self.check_near_connection(*args)
            if j == 0 and not next_checks:
                i += 2
                last_i_0 = i
                if i > 12:
                    return False

            elif j == 0 and len(next_checks) == 1:
                checked.append((i, j))
                i, j = next_checks[0]

            elif j != 0 and len(next_checks) == 1:
                if last_i_0 == 11:
                    return False
                else:
                    last_i_0 += 2
                    i, j = last_i_0, 0

            elif j != 0 and len(next_checks) == 2:
                checked.append((i, j))
                if next_checks[0] not in checked:
                    i, j = next_checks[0]
                elif next_checks[1] not in checked:
                    i, j = next_checks[1]
                else:
                    if last_i_0 == 11:
                        return False
                    else:
                        last_i_0 += 2
                        i, j = last_i_0, 0

            elif j != 0 and (3 <= len(next_checks) <= 4):
                checked.append((i, j))
                for check in next_checks:
                    if check not in checked:
                        if self.check_win_connection(player,
                                                     check_grid,
                                                     check,
                                                     checked):
                            return True
                        checked.append(check)
                else:
                    if last_i_0 == 11:
                        return False
                    else:
                        last_i_0 += 2
                        i, j = last_i_0, 0

            else:
                if last_i_0 == 11:
                    return False
                else:
                    last_i_0 += 2
                    i, j = last_i_0, 0

            if j >= 11:
                return True

    def check_win(self) -> str | None:
        if self.check_win_connection(self.player1):
            return self.player1
        elif self.check_win_connection(self.player2):
            return self.player2
        return None
