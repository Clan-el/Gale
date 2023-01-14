class Grid:
    def __init__(self, player1, player2, size) -> None:
        self.player1 = player1
        self.player2 = player2
        self.size = size
        self.clear_grid()

    def clear_grid(self):
        grid = []
        for _ in range(self.size):
            grid.append([None] * self.size)
        for row in range(self.size):
            for column in range(self.size):
                if ((row * self.size) + column) % 2 == 1:
                    if row % 2 == 0:
                        grid[row][column] = self.player2
                    else:
                        grid[row][column] = self.player1
        self.grid = grid

    def get_grid(self) -> list[list[str | None]]:
        return self.grid

    def get_cell(self, point: tuple[int, int]) -> str | None:
        return self.grid[point[0]][point[1]]

    def change_cell(self, point: tuple[int, int], player: str):
        row, column = point
        self.grid[row][column] = player

    def set_grid(self, new_grid):
        self.size = len(new_grid)
        self.grid = new_grid

    def free_cells(self) -> list:
        free_cell_list = []
        for row in range(1, self.size - 1):
            for column in range(1, self.size - 1):
                if self.grid[row][column] is None:
                    free_cell_list.append((row, column))
        return free_cell_list

    def check_near_connection(self,
                              point: tuple[int, int],
                              player: str,
                              check_grid=None) -> list:

        row, column = point
        check_grid = self.grid if check_grid is None else check_grid
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

        check_grid = self.grid[:] if check_grid is None else check_grid
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
