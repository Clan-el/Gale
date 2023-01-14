import sys
from grid_tests import grid, gridA, gridB, gridB2
sys.path.insert(0, '.')
from logic import Game
from bot import easy_bot_move
from interface import Interface
# sys.path.insert(0, '.')


def test_check_near_connection():
    eee = Game()
    eee.grid._set_grid(gridA)
    aaa = eee.check_near_connection((7, 4), "C")
    assert aaa == [(7, 5), (8, 4), (6, 4), (7, 3)]


def test_check_connection_none():
    game = Game()
    game.grid._set_grid(grid)
    assert game.check_win_connection("C") is False
    assert game.check_win_connection("N") is False


def test_check_connection_A():
    game = Game()
    game.grid._set_grid(gridA)
    assert game.check_win_connection("C") is True
    assert game.check_win_connection("N") is False


def test_check_connection_B():
    game = Game()
    game.grid._set_grid(gridB)
    assert game.check_win_connection("C") is False
    assert game.check_win_connection("N") is True


def test_check_win_none():
    game = Game()
    game.grid._set_grid(grid)
    assert game.check_win() is None
    gameB2 = Game()
    gameB2.grid._set_grid(gridB2)
    assert gameB2.check_win() is None


def test_check_win_A():
    game = Game()
    game.grid._set_grid(gridA)
    assert game.check_win() == game.player1


def test_check_win_B():
    game = Game()
    game.grid._set_grid(gridB)
    assert game.check_win() == game.player2


def test_check_win_random():
    """
    Gra w Gale nie może zakończyć się remisem, któryś z graczy musi wygrać,
    stąd test sprawdzający czy przez 101 rozgrywek z powodu błędu algorytmu
    występuje remis, czyli game.check_win() == None
    """
    game = Game()
    games = 0
    max_moves = ((game.size-2)//2)*(game.size - 2 + 1) + 1
    while games <= 100:
        moves = 0
        while moves < max_moves and game.check_win() is None:
            player = "C" if moves % 2 == 0 else "N"
            cell_cords = easy_bot_move(game.grid)
            game.grid.change_cell(cell_cords, player)
            moves += 1
        print(game.check_win(), moves)
        if game.check_win() is None:
            assert game.check_win() is not None
        else:
            game.grid.clear_grid()
            games += 1
    assert games == 101


if __name__ == "__main__":
    """
    Analogiczne do test_check_win_random, ale z reprezentacją graficzną siatki
    """
    game = Game()
    games = 0
    max_moves = ((game.size-2)//2)*(game.size - 2 + 1) + 1
    while games <= 100:
        game.grid.clear_grid()
        moves = 0
        while moves < max_moves and game.check_win() is None:
            player = game.player1 if moves % 2 == 0 else game.player2
            cell_cords = easy_bot_move(game.grid)
            game.grid.change_cell(cell_cords, player)
            moves += 1
        print(game.check_win(), moves)
        if game.check_win() is None:
            game.interface = Interface(game.grid)
            game.interface.draw_board(game.interface.board)
        else:
            games += 1
        games += 1
