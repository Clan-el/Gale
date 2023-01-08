import pygame, pygame.gfxdraw
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from logic import Game
import grid
from random import randint

def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font("arial")
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    # text_surface = font.render(text, True, white)

    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)


def draw_board(board):
    for i in range(13):
        for j in range(13):
            if game.get_cell((i, j)) == "C":
                board[i][j] = red
            elif game.get_cell((i, j)) == "N":
                board[i][j] = blue

            x = j * cell_size + circle_radious + offset
            y = i * cell_size + circle_radious + offset

            drawing_arguments = screen, x, y, circle_radious, board[i][j]
            pygame.gfxdraw.filled_circle(*drawing_arguments)
            pygame.gfxdraw.aacircle(*drawing_arguments)

            if (board[i][j] == white and 1<=i<=11 and 1<=j<=11):
                pygame.gfxdraw.filled_circle(screen, x, y, 2, grey)
                pygame.gfxdraw.aacircle(screen, x, y, 2, grey)


def clear_board():
    board = []
    for _ in range(13):
        board.append([white] * 13)
    return board


def endgame_box():
    draw_box(320, 110)

    winner = "Czerwony" if game.check_win() == "C" else "Niebieski"
    text = f"Wygrał gracz {winner}"
    draw_text(screen, text, 18, screen_width//2, screen_height//2-15)
    text = "Kliknij aby kontynuować lub wyjdź"
    draw_text(screen, text, 18, screen_width//2, screen_height//2+15)


def draw_box(rect_width: int, rect_height: int):
    rect_x = (screen_width - rect_width) // 2
    rect_y = (screen_height - rect_height) // 2
    rectangle = (rect_x, rect_y, rect_width, rect_height)
    param = screen, light_grey, rectangle, 0, 20
    pygame.draw.rect(*param)
    param = screen, black, rectangle, 5, 20
    pygame.draw.rect(*param)


class Button:
    def __init__(self, text:str, rectangle:tuple[int,int,int,int], offset:int):
        rect_x, rect_y, rect_width, rect_height = rectangle
        rect_y += offset
        rectangle = rect_x, rect_y, rect_width, rect_height
        pygame.draw.rect(screen, white, rectangle, 0, 20)
        pygame.draw.rect(screen, black, rectangle, 2, 20)

        draw_text(screen, text, 18, screen_width//2, screen_height//2+offset)

        (self._rect_x, self._rect_y, self._rect_width,
        self._rect_height) = rectangle

    def inside(self, mouse: tuple[int, int]):
        mouse_x, mouse_y = mouse
        if self._rect_x < mouse_x < self._rect_x + self._rect_width:
            if self._rect_y < mouse_y < self._rect_y + self._rect_height:
                return True
        return False


# Set the sizes
screen_width, screen_height = 670, 670
offset = 10
cell_size = 50
circle_radious = 23

# Set the colors for the cells
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (100, 100, 100)
light_grey = (190, 190, 190)


pygame.init()
pygame.display.set_caption("Shannon switching - Gale")
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill(white)
board = clear_board()
game = Game(grid.gridB2)
moves = 0
LEFT = 1


stages = ("starting", "running", "over", "exit")
current_stage = "starting"


draw_box(300, 300)
text = "Wybierz tryb gry:"
draw_text(screen, text, 18, screen_width//2, screen_height//2-100)

rect_width, rect_height = 210, 45
rect_x = (screen_width - rect_width) // 2
rect_y = (screen_height - rect_height) // 2 + 2
rectangle = (rect_x, rect_y, rect_width, rect_height)

Button1 = Button("2 Graczy", rectangle, -40)
Button2 = Button("vs Komputer - Łatwy", rectangle, +30)
Button3 = Button("vs Komputer - Trudny", rectangle, +100)
pygame.display.update()

while current_stage == stages[0]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_stage = stages[3]

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if Button1.inside(pygame.mouse.get_pos()):
                current_stage = stages[1]
            elif Button2.inside(pygame.mouse.get_pos()):
                print("BBB")
            elif Button3.inside(pygame.mouse.get_pos()):
                print("CCC")



screen.fill(white)
while current_stage == stages[1]:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            current_stage = stages[3]

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            # event.button
            mouse_x, mouse_y = pygame.mouse.get_pos()
            column = (mouse_x - offset) // cell_size
            row = (mouse_y - offset) // cell_size
            first_strip = cell_size + offset
            last_strip = cell_size*12 + offset

            if (first_strip < mouse_x < last_strip and
                first_strip < mouse_y < last_strip and
                game.get_cell((row, column)) is None):

                moves += 1
                if moves % 2 == 1:
                    game.change_cell((row, column), "C")
                else:
                    game.change_cell((row, column), "N")

    draw_board(board)
    pygame.display.update()

    if game.check_win():
        current_stage = stages[2]
        ggg = endgame_box()
        pygame.display.update()

        while current_stage == stages[2]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    current_stage = stages[3]

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    game.clear_grid()
                    moves = 0
                    current_stage = stages[1]
                    screen.fill(white)
                    board = clear_board()

pygame.quit()