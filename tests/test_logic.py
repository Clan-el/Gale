import sys
sys.path.insert(0,'.')

from grid import grid, gridA, gridB, gridB2
from logic import Game
from bot import easy_bot_move
from interface import Interface


def test_check_near_connection():
    eee = Game(gridA)
    aaa = eee.check_near_connection((7, 4), "C")
    assert aaa == [(7, 5), (8, 4), (6, 4), (7, 3)]

def test_check_connection_none():
    game = Game(grid)
    assert game.check_win_connection("C") == False
    assert game.check_win_connection("N") == False

def test_check_connection_A():
    gameA = Game(gridA)
    assert gameA.check_win_connection("C") == True
    assert gameA.check_win_connection("N") == False

def test_check_connection_B():
    gameB = Game(gridB)
    assert gameB.check_win_connection("C") == False
    assert gameB.check_win_connection("N") == True

def test_check_win_none():
    game = Game(grid)
    assert game.check_win() == None
    gameB2 = Game(gridB2)
    assert gameB2.check_win() == None

def test_check_win_A():
    gameA = Game(gridA)
    assert gameA.check_win() == "C"

def test_check_win_B():
    gameB = Game(gridB)
    assert gameB.check_win() == "N"


def test_check_win_random():
    """
    Gra w Gale nie może zakończyć się remisem, któryś z graczy musi wygrać,
    stąd test sprawdzający czy przez 101 rozgrywek z powodu błędu algorytmu
    występuje remis, czyli game.check_win() == None
    """
    game = Game()
    games = 0
    while games <= 100:
        i = 0
        while i < 61 and game.check_win() is None:
            if i == 58:
                pass
            player = "C" if i % 2 == 0 else "N"
            cell_cords = easy_bot_move(game.get_grid())
            game.change_cell(cell_cords, player)
            i += 1
        print(game.check_win(), i)
        if game.check_win() is None:
            assert game.check_win() is not None
        else:
            game = Game()
            games +=1
    assert games == 101


if __name__ == "__main__":
    """
    Analogiczne do test_check_win_random, ale z reprezentacją graficzną siatki
    """
    game = Game(grid)
    games = 0
    while games <= 100:
        game.clear_grid()
        i = 0
        while i < 61 and game.check_win() is None:
            player = "C" if i % 2 == 0 else "N"
            cell_cords = easy_bot_move(game.get_grid())
            game.change_cell(cell_cords, player)
            i += 1
        print(game.check_win(), i)
        if game.check_win() is None:
            interface = Interface(game)
            stage = "2_players"
            while stage != "exit":
                condition = stage == "2_players" or stage == "over"
                stage = interface.two_players(stage) if condition else stage
            interface.close()
        else:
            games +=1
