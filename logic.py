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
  ['A', None, 'A', None, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
]



def check_short_connection(point, pattern, player):
    neighbors = []
    i, j = point
    if j + 1 <= 12 and pattern[i][j+1] == player:
        neighbors.append((i, j+1))
    if i + 1 <= 12 and pattern[i+1][j] == player:
        neighbors.append((i+1, j))
    if i - 1 >= 0 and pattern[i-1][j] == player:
        neighbors.append((i-1, j))
    if j - 1 >= 0 and pattern[i][j-1] == player:
        neighbors.append((i, j-1))
    return neighbors

checked = []
def check_connection(pattern, player, cords=None):

    if cords == None:
        i = 1
        j = 0
    else:
        i = cords[0]
        j = cords[1]

    while True == True:
        print(i, j)
        next_checks = check_short_connection((i, j), pattern, player)

        if j == 0 and len(next_checks) == 0:
            i += 2
        elif j == 0 and len(next_checks) == 1:
            checked.append((i, j))
            i, j = next_checks[0]
        elif j != 0 and len(next_checks) == 1:
            return None
        elif j != 0 and len(next_checks) == 2:
            checked.append((i, j))
            if next_checks[0] not in checked:
                i, j = next_checks[0]
            elif next_checks[1] not in checked:
                i, j = next_checks[1]
            else:
                return None

        elif j != 0 and (len(next_checks) == 3 or len(next_checks) == 4):
            checked.append((i, j))
            for x in range(len(next_checks)):
                if next_checks[x] not in checked:
                    if check_connection(pattern, player, next_checks[x]) is not None:
                        return player
                    else:
                        checked.append(next_checks[x])

        else:
            print("coś nie działa")
            return None

        if j >= 11:
            print(i, j)
            return player




# print(check_connection(pattern2, "A"))



class Game:
    def __init__(self) -> None:
        self.board = pattern2
        pass

board = Game()