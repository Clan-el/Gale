from random import seed, choice
from datetime import datetime
from grid import Grid
from interface import Interface
import multiprocessing

now = datetime.now()
seed(now.minute ** now.second - now.microsecond)


def my_copy(array):
    return [[elem for elem in sublist] for sublist in array]


def easy_bot_move(grid: Grid) -> tuple[int, int]:
    return choice(grid.free_cells())


def hard_bot_move(grid: Grid, player, interface: Interface = None):
    available_moves = grid.free_cells()
    best_move = None
    best_score = float('-inf')
    simulations = 1600 - 9*grid.size**2

    for count, move in enumerate(available_moves):
        percent = ((count*100)/len(available_moves))

        if interface is not None:
            full_player = "Czerwony" if player == grid.player1 else "Niebieski"
            text = f"Gracz {full_player} główkuje: {percent:.2f}%"
            interface.change_caption(text)

        grid.change_cell(move, player)
        score = monte_carlo_tree_search(grid, player, simulations)
        grid.change_cell(move, None)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move


# def monte_carlo_tree_search(grid: Grid, player, simulations):
#     wins = 0
#     for _ in range(simulations):
#         # grid_copy = Grid(grid.player1, grid.player2, grid.size)
#         # grid_copy.set_grid([row[:] for row in grid.get_grid()])
#         arguments = (my_copy(grid.grid), grid.player1,
#                      grid.player2, grid.size, player)

#         winner = simulate_random_game(arguments)
#         if winner == 1:
#             wins += 1
#     return wins / simulations


def monte_carlo_tree_search(grid: Grid, player, simulations):
    wins = 0
    with multiprocessing.Pool() as pool:
        arguments = (my_copy(grid.grid), grid.player1,
                     grid.player2, grid.size, player)
        list_comp = [arguments for _ in range(simulations)]
        wins = sum(pool.map(simulate_random_game, list_comp))
    return wins / simulations


def simulate_random_game(args):
    grid_copy, player1, player2, size, player = args
    current_player = player
    grid = Grid(player1, player2, size)
    grid.set_grid(grid_copy)
    while grid.check_win() is None and grid.free_cells():
        available_moves = grid.free_cells()
        move = choice(available_moves)
        grid.change_cell(move, current_player)
        current_player = player1 if current_player == player2 else player2
    if grid.check_win() == player:
        return 1
    else:
        return 0
