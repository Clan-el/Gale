from random import randint, seed
from datetime import datetime


def easy_bot_move(game):
    now = datetime.now()
    seed(now.minute * now.second * now.microsecond)
    while True:
        row, column = randint(1, 11), randint(1, 11)
        if game.get_cell((row, column)) is None:
            return (row, column)

def hard_bot_mode(game):
    pass