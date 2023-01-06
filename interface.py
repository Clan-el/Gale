import pygame, pygame.gfxdraw
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from logic import Game
import grid


def draw_text(surf, text, size, x, y):
    font_name = pygame.font.match_font("arial")
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)


def draw_board(board):
    for i in range(13):
        for j in range(13):
            if game.get_tile((i, j)) == 'A':
                board[i][j] = red_color
            elif game.get_tile((i, j)) == 'B':
                board[i][j] = blue_color

            x = j * cell_size + circle_radious + off_set
            y = i * cell_size + circle_radious + off_set

            drawing_arguments = screen, x, y, circle_radious, board[i][j]
            pygame.gfxdraw.filled_circle(*drawing_arguments)
            pygame.gfxdraw.aacircle(*drawing_arguments)

            if (board[i][j] == white_color and 1<=i<=11 and 1<=j<=11):
                pygame.gfxdraw.filled_circle(screen, x, y, 2, grey_color)
                pygame.gfxdraw.aacircle(screen, x, y, 2, grey_color)


def clear_board():
    board = []
    for _ in range(13):
        board.append([white_color] * 13)
    return board


def endgame_box():
    rect_width = 300
    rect_height = 100
    rect_x = (screen_width - rect_width) // 2
    rect_y = (screen_height - rect_height) // 2
    param = screen, green_color, (rect_x, rect_y, rect_width, rect_height)
    pygame.draw.rect(*param)

    text = f"Wygrał gracz {game.check_win()}"
    draw_text(screen, text, 18, screen_width//2, screen_height//2-15)
    text = "Kliknij aby kontynuować lub wyjdź"
    draw_text(screen, text, 18, screen_width//2, screen_height//2+15)


pygame.init()
pygame.display.set_caption("Shannon switching - Gale")
screen_width = 670
screen_height = 670
screen = pygame.display.set_mode((screen_width, screen_height))
off_set = 10
cell_size = 50
circle_radious = 23

# Set the colors for the cells
white_color = (255, 255, 255)
black_color = (0, 0, 0)
blue_color = (0, 0, 255)
red_color = (255, 0, 0)
grey_color = (100, 100, 100)
green_color = (0, 255, 0)
screen.fill(white_color)


board = clear_board()
game = Game(grid.gridA2)
moves = 0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            column = (mouse_x - off_set) // cell_size
            row = (mouse_y - off_set) // cell_size
            first_strip = cell_size + off_set
            last_strip = cell_size*12 + off_set

            if (first_strip < mouse_x < last_strip and
                first_strip < mouse_y < last_strip and
                game.get_tile((row, column)) is None):

                moves += 1
                if moves % 2 == 1:
                    game.change_tile((row, column), "A")
                else:
                    game.change_tile((row, column), "B")

    draw_board(board)
    pygame.display.update()

    if game.check_win():
        running = False
        endgame_box()
        pygame.display.update()
        while running is False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    game.clear_grid()
                    moves = 0
                    running = True
                    screen.fill(white_color)
                    board = clear_board()

pygame.quit()