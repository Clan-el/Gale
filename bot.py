from random import seed, choice
from datetime import datetime
from grid import Grid

now = datetime.now()
seed(now.minute ** now.second - now.microsecond)

def easy_bot_move(grid: Grid) -> tuple[int, int]:
    return choice(grid.free_cells())


def hard_bot_move(game, game_copy):
    available_moves = game.grid.free_cells()
    best_move = None
    best_score = float('-inf')
    simulations = 1600 - 9*game.size**2
    for count, move in enumerate(available_moves):
        percent = ((count*100)/len(available_moves))
        game.interface.change_caption(f"Gracz Niebieski główkuje: {percent:.2f}%")
        game.grid.change_cell(move, game.player2)
        score = monte_carlo_tree_search(game, game_copy, simulations)
        game.grid.change_cell(move, None)

        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def monte_carlo_tree_search(game, game_copy, simulations):
    wins = 0
    for _ in range(simulations):
        grid_copy = Grid(game.player1, game.player2, game.size)
        grid_copy._set_grid([row[:] for row in game.grid.get_grid()])
        winner = simulate_random_game(grid_copy, game_copy)
        if winner == game.player2:
            wins += 1
    return wins / simulations

def simulate_random_game(grid: Grid, game_copy):
    current_player = grid.player1
    game_copy.set_grid(grid)
    while game_copy.check_win() is None and grid.free_cells():
        available_moves = grid.free_cells()
        move = choice(available_moves)
        grid.change_cell(move, current_player)
        current_player = grid.player1 if current_player == grid.player2 else grid.player2
    return game_copy.check_win()
