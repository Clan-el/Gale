import sys
from grid_tests import grid0, gridA, gridB, gridB2
from time import time
sys.path.insert(0, '.')
from grid import Grid
from bot import easy_bot_move, hard_bot_move
from interface import Interface


def test_check_near_connection():
    grid = Grid("C", "N", 13)
    grid.set_grid(gridA)
    near_list = grid.check_near_connection((7, 4), "C")
    assert near_list == [(7, 5), (8, 4), (6, 4), (7, 3)]


def test_check_connection_none():
    grid = Grid("C", "N", 13)
    grid.set_grid(grid0)
    assert grid.check_win_connection("C") is False
    assert grid.check_win_connection("N") is False


def test_check_connection_A():
    grid = Grid("C", "N", 13)
    grid.set_grid(gridA)
    assert grid.check_win_connection("C") is True
    assert grid.check_win_connection("N") is False


def test_check_connection_B():
    grid = Grid("C", "N", 13)
    grid.set_grid(gridB)
    assert grid.check_win_connection("C") is False
    assert grid.check_win_connection("N") is True


def test_check_win_none():
    grid = Grid("C", "N", 13)
    grid.set_grid(grid0)
    assert grid.check_win() is None
    grid = Grid("C", "N", 13)
    grid.set_grid(gridB2)
    assert grid.check_win() is None


def test_check_win_A():
    grid = Grid("C", "N", 13)
    grid.set_grid(gridA)
    assert grid.check_win() == grid.player1


def test_check_win_B():
    grid = Grid("C", "N", 13)
    grid.set_grid(gridB)
    assert grid.check_win() == grid.player2


def test_check_win_random():
    """
    Gra w Gale nie może zakończyć się remisem, któryś z graczy musi wygrać,
    stąd test sprawdzający czy przez 101 rozgrywek z powodu błędu algorytmu
    występuje remis, czyli game.check_win() == None
    """
    grid = Grid("C", "N", 13)
    games = 0
    max_moves = ((grid.size-2)//2)*(grid.size - 2 + 1) + 1

    while games <= 100:
        moves = 0
        while moves < max_moves and grid.check_win() is None:
            player = "C" if moves % 2 == 0 else "N"
            cell_cords = easy_bot_move(grid)
            grid.change_cell(cell_cords, player)
            moves += 1
        print(grid.check_win(), moves)
        if grid.check_win() is None:
            assert grid.check_win() is not None
        else:
            grid.clear_grid()
            games += 1
    assert games == 101


if __name__ == "__main__":
    """
    Analogiczne do test_check_win_random,
    ale z reprezentacją graficzną siatki w razie nie powodzenia.
    Wypisuje także zwycięzcę, ilość ruchów oraz czas rozgrywki.
    """
    grid = Grid("C", "N", 9)
    games = 0
    max_moves = ((grid.size-2)//2)*(grid.size - 2 + 1) + 1

    while games <= 10:
        moves = 0
        initialTime = time()
        while moves < max_moves and grid.check_win() is None:
            player = grid.player1 if moves % 2 == 0 else grid.player2
            # cell_cords = easy_bot_move(grid)
            cell_cords = hard_bot_move(grid, player)
            grid.change_cell(cell_cords, player)
            moves += 1

        print(grid.check_win(), moves)
        print(time() - initialTime)

        if grid.check_win() is None:
            interface = Interface(grid)
            interface.draw_board(interface.board)
            interface.wait_for_closing()
        else:
            grid.clear_grid()
        games += 1
