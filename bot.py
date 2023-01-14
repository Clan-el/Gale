from random import seed, choice
from datetime import datetime
from grid import Grid
from interface import Interface

now = datetime.now()
seed(now.minute ** now.second - now.microsecond)

def easy_bot_move(grid: Grid) -> tuple[int, int]:
    return choice(grid.free_cells())


def hard_bot_move(grid: Grid, interface: Interface=None):
    available_moves = grid.free_cells()
    best_move = None
    best_score = float('-inf')
    simulations = 1600 - 9*grid.size**2

    for count, move in enumerate(available_moves):
        percent = ((count*100)/len(available_moves))

        if interface is not None:
            text = f"Gracz Niebieski główkuje: {percent:.2f}%"
            interface.change_caption(text)

        grid.change_cell(move, grid.player2)
        score = monte_carlo_tree_search(grid, simulations)
        grid.change_cell(move, None)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def monte_carlo_tree_search(grid: Grid, simulations):
    wins = 0
    for _ in range(simulations):
        grid_copy = Grid(grid.player1, grid.player2, grid.size)
        grid_copy.set_grid([row[:] for row in grid.get_grid()])
        winner = simulate_random_game(grid_copy)
        if winner == grid.player2:
            wins += 1
    return wins / simulations

def simulate_random_game(grid: Grid):
    current_player = grid.player1
    while grid.check_win() is None and grid.free_cells():
        available_moves = grid.free_cells()
        move = choice(available_moves)
        grid.change_cell(move, current_player)

        condition = current_player == grid.player2
        current_player = grid.player1 if condition else grid.player2
    return grid.check_win()
