from random import seed, choice
from datetime import datetime
from grid import Grid


def easy_bot_move(grid: Grid) -> tuple[int, int]:
    now = datetime.now()
    seed(now.minute ** now.second - now.microsecond)
    return choice(grid.free_cells())


def hard_bot_mode(grid: Grid) -> tuple[int, int]:
    pass
