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

patternA = [
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', None, 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', 'A', 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', None, 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
]

patternB = [
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', 'B', 'A', 'B', 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', 'B', 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', 'B', 'A', None, 'A', 'B', 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', 'B', 'B', 'B', 'B', 'B', 'B', None, 'B', None],
  ['A', None, 'A', 'B', 'A', None, 'A', None, 'A', 'B', 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', None, 'A', 'B', 'A', None, 'A', None, 'A', 'B', 'A', None, 'A'],
  [None, 'B', 'B', 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
  ['A', 'B', 'A', None, 'A', None, 'A', None, 'A', 'B', 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', 'B', 'B', None],
  ['A', 'B', 'A', None, 'A', None, 'A', None, 'A', None, 'A', None, 'A'],
  [None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None, 'B', None],
]


def check_near_connection(point, pattern, player):
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
        if player == 'B':
            rotated = list(zip(*pattern))[::-1]
            rotated = [list(elem) for elem in rotated]
            pattern = rotated
    else:
        i = cords[0]
        j = cords[1]

    while True == True:
        print(i, j)
        next_checks = check_near_connection((i, j), pattern, player)

        if j == 0 and len(next_checks) == 0:
            i += 2
            if i > 12:
                return None
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
                print("tak dla testu")
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
            return None

        if j >= 11:
            print(i, j)
            return player



print(check_connection(patternB, "A"))
print(check_connection(patternB, "B"))



class Game:
    def __init__(self) -> None:
        self.board = patternB
        pass

    pass

game = Game()