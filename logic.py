from grid import grid, gridA, gridB, gridB2

class Game:
    def __init__(self, game_grid=None):
        self._grid = grid if game_grid is None else game_grid

    def get_tile(self, point: tuple[int, int]):
        return self._grid[point[0]][point[1]]

    def change_tile(self, point: tuple[int, int], player: str):
        x, y = point
        self._grid[x][y] = player

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
                             checked=None):

        check_grid = self._grid[:] if check_grid is None else check_grid
        checked = checked if checked is not None else []

        if cords == None:
            i, j = 1, 0
            if player == 'B':
                rotated = list(zip(*check_grid))[::-1]
                rotated = [list(elem) for elem in rotated]
                check_grid = rotated
        else:
            i, j = cords

        while True:
            next_checks = self.check_near_connection((i, j), player, check_grid)

            if j == 0 and not next_checks:
                i += 2
                if i > 12:
                    return None

            elif j == 0 and len(next_checks) == 1:
                checked.append((i, j))
                i, j = next_checks[0]

            elif j != 0 and len(next_checks) == 1:
                return None

            elif j != 0 and len(next_checks) == 2:
                checked.append((i, j))
                if next_checks[0] not in checked:
                    i, j = next_checks[0]
                elif next_checks[1] not in checked:
                    i, j = next_checks[1]
                else:
                    return None

            elif j != 0 and (3 <= len(next_checks) <= 4):
                checked.append((i, j))
                for check in next_checks:
                    if check not in checked:
                        if self.check_win_connection(player,
                                                     check_grid,
                                                     check,
                                                     checked):
                            return player
                        checked.append(check)
                return None

            else:
                return None

            if j >= 11:
                return player

    def check_win(self):
        if self.check_win_connection("A") == "A":
            return "A"
        elif self.check_win_connection("B") == "B":
            return "B"
        return None


if __name__ == "__main__":
    game = Game(grid)
    gameA = Game(gridA)
    gameB = Game(gridB)
    print(gameA.check_win_connection("A"))
    print(gameB.check_win_connection("B"))

    print(gameA.check_win())