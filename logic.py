# import networkx.algorithms.connectivity as con

pattern = [
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
]

pattern2 = [
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', 'A', 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', 'A', 'A', 'A', 'A', None, 'A', 'A', 'A', 'A', 'A'],
  [None, 'B', None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', 'A', 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', 'A', 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', 'A', 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', 'A', 'A', 'A', 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
]
class Game:
    def __init__(self) -> None:
        self.board = pattern2
        pass

board = Game()

def check_short_connection(point, pattern, player):
    neighbors = []
    i, j = point
    if pattern[i+1][j] == player:
        neighbors.append((i+1, j))
    if pattern[i-1][j] == player:
        neighbors.append((i-1, j))
    if pattern[i][j+1] == player:
        neighbors.append((i, j+1))
    if pattern[i][j-1] == player:
        if j - 1 >= 0:
            neighbors.append((i, j-1))
    return neighbors


def check_connection(pattern, player, cords=None):
    checked = []
    if cords == None:
        i = 1
        j = 0

    while True == True:
        print(i, j)
        next_checks = check_short_connection((i, j), pattern, player)

        if j == 0 and len(next_checks) == 0:
            i += 2
        elif j == 0 and len(next_checks) == 1:
            checked.append((i, j))
            i, j = next_checks[0]
        elif j != 0 and len(next_checks) == 2:
            checked.append((i, j))
            if next_checks[0] not in checked:
                i, j = next_checks[0]
            else:
                i, j = next_checks[1]
        elif j != 0 and len(next_checks) > 2:
            return "niedokończony pomysł"
        else:
            return None

        if j == 11:
            print(i, j)
            return f'Player {player} won!'




print(check_connection(pattern2, "A"))

