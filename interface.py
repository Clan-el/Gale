import pygame
import pygame.gfxdraw
from logic import Game

game = Game()
pygame.init()


screen_width = 660
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Shannon switching")

off_set = 10
cell_size = 50
circle_radious = 23

# Set the colors for the cells
white_color = (255, 255, 255)
blue_color = (0, 0, 255)
red_color = (255, 0, 0)
grey_color = (100,100,100)
screen.fill(white_color)

# Initialize the board as a 2D array of white cells
board = []
for _ in range(13):
    board.append([white_color] * 13)

times_clicked = 0  # moves


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            column = (mouse_x - off_set) // cell_size
            row = (mouse_y - off_set) // cell_size
            if (cell_size + off_set <= mouse_x <= cell_size*12 + off_set and
                cell_size + off_set <= mouse_y <= cell_size*12 + off_set and
                game.get_tile((row, column)) is None):

                if times_clicked % 2 == 0:
                    game.change_tile((row, column), "A")
                    times_clicked += 1
                elif times_clicked % 2 == 1:
                    game.change_tile((row, column), "B")
                    times_clicked += 1


    # Draw the board
    for i in range(13):
        for j in range(13):
            if game.get_tile((i, j)) == 'A':
                board[i][j] = red_color
            elif game.get_tile((i, j)) == 'B':
                board[i][j] = blue_color

            x = j * cell_size + circle_radious + off_set
            y = i * cell_size + circle_radious + off_set

            if board[i][j] != white_color:
                drawing_arguments = screen, x, y, circle_radious, board[i][j]
                pygame.gfxdraw.filled_circle(*drawing_arguments)
                pygame.gfxdraw.aacircle(*drawing_arguments)

            if (board[i][j] == white_color and 1<=i<=11 and 1<=j<=11):
                pygame.gfxdraw.filled_circle(screen, x, y, 2, grey_color)
                pygame.gfxdraw.aacircle(screen, x, y, 2, grey_color)




    pygame.display.update()
pygame.quit()