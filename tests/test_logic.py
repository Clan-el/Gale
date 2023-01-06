import sys
sys.path.insert(0,'.')

from grid import grid, gridA, gridB, gridB2
from logic import Game


def test_check_near_connection():
    eee = Game(gridA)
    aaa = eee.check_near_connection((7, 4), "A")
    assert aaa == [(7, 5), (8, 4), (6, 4), (7, 3)]

def test_check_connection_none():
    game = Game(grid)
    assert game.check_win_connection("A", game._grid) == None
    assert game.check_win_connection("B", game._grid) == None

def test_check_connection_A():
    gameA = Game(gridA)
    assert gameA.check_win_connection("A", gameA._grid) == "A"
    assert gameA.check_win_connection("B", gameA._grid) == None

def test_check_connection_B():
    gameB = Game(gridB)
    assert gameB.check_win_connection("A") == None
    assert gameB.check_win_connection("B") == "B"

def test_check_win_none():
    game = Game(grid)
    assert game.check_win() == None
    gameB2 = Game(gridB2)
    assert gameB2.check_win() == None

def test_check_win_A():
    gameA = Game(gridA)
    assert gameA.check_win() == "A"

def test_check_win_B():
    gameB = Game(gridB)
    assert gameB.check_win() == "B"