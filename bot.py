from random import randint, seed
from datetime import datetime


def easy_bot_move(grid: list[list[str | None]]) -> tuple[int, int]:
    now = datetime.now()
    seed(now.minute * now.second * now.microsecond)
    while True:
        row, column = randint(1, 11), randint(1, 11)
        if grid[row][column] is None:
            return (row, column)


def hard_bot_mode(game):
    pass
