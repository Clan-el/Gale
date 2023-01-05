from grid import grid, gridA, gridB


# def check_near_connection(point, grid, player):
#     i, j = point
#     neighbors = [(i + x, j + y) for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]
#                    if (0 <= i + x <= 12 and 0 <= j + y <= 12 and
#                    grid[i + x][j + y] == player)]
#     return neighbors


# def check_win_connection(grid, player, cords=None, checked=None):
#     if cords == None:
#         i = 1
#         j = 0
#         if player == 'B':
#             rotated = list(zip(*grid))[::-1]
#             rotated = [list(elem) for elem in rotated]
#             grid = rotated
#     else:
#         i, j = cords

#     checked = checked if checked is not None else []

#     while True:
#         next_checks = check_near_connection((i, j), grid, player)

#         if j == 0 and not next_checks:
#             i += 2
#             if i > 12:
#                 return None
#         elif j == 0 and len(next_checks) == 1:
#             checked.append((i, j))
#             i, j = next_checks[0]
#         elif j != 0 and len(next_checks) == 1:
#             return None
#         elif j != 0 and len(next_checks) == 2:
#             checked.append((i, j))
#             if next_checks[0] not in checked:
#                 i, j = next_checks[0]
#             elif next_checks[1] not in checked:
#                 i, j = next_checks[1]
#             else:
#                 print("tak dla testu")
#                 return None
#         elif j != 0 and (3 <= len(next_checks) <= 4):
#             checked.append((i, j))
#             for x in range(len(next_checks)):
#                 if next_checks[x] not in checked:
#                     if (check_win_connection(grid, player, next_checks[x],
#                         checked) is not None):
#                         return player
#                     else:
#                         checked.append(next_checks[x])
#         else:
#             return None

#         if j >= 11:
#             return player


class Game:
    def __init__(self) -> None:
        self.grid = gridA

    def check_near_connection(self, point, player):
        i, j = point
        neighbors = [(i + x, j + y) for x, y in [(0, 1), (1, 0),
                    (0, -1), (-1, 0)]
                    if (0 <= i + x <= 12 and 0 <= j + y <= 12 and
                    self.grid[i + x][j + y] == player)]
        return neighbors

    def check_win_connection(self, player, cords=None, checked=None):
        if cords == None:
            i = 1
            j = 0
            if player == 'B':
                rotated = list(zip(*self.grid))[::-1]
                rotated = [list(elem) for elem in rotated]
                self.grid = rotated
        else:
            i, j = cords

        checked = checked if checked is not None else []

        while True:
            next_checks = self.check_near_connection((i, j), player)

            if j == 0 and not next_checks:
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
                    return None
            elif j != 0 and (3 <= len(next_checks) <= 4):
                checked.append((i, j))
                for x in range(len(next_checks)):
                    if next_checks[x] not in checked:
                        if (self.check_win_connection(player, next_checks[x],
                            checked) is not None):
                            return player
                        else:
                            checked.append(next_checks[x])
            else:
                return None
            if j >= 11:
                return player

    pass

game = Game()

print(game.check_win_connection("A"))
print(game.check_win_connection("B"))