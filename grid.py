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

    def _set_grid(self, new_grid):
        self.size = len(new_grid)
        self.grid = new_grid

    def free_cells(self) -> list:
        free_cell_list = []
        for row in range(1, self.size - 1):
            for column in range(1, self.size - 1):
                if self.grid[row][column] is None:
                    free_cell_list.append((row, column))
        return free_cell_list
