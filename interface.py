import pygame
import pygame.gfxdraw
from logic import Game

game = Game()
pygame.init()

# Set the width and height of the screen
screen_width = 660
screen_height = 660
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title of the window
pygame.display.set_caption("Shannon switching")

# Set the dimensions of each cell on the board
off_set = 10
cell_size = 50
circle_radious = 23

# Set the colors for the cells
white_color = (255, 255, 255)
blue_color = (0, 0, 255)
red_color = (255, 0, 0)
screen.fill(white_color)

# Initialize the board as a 2D array of white cells
board = []
for _ in range(13):
    board.append([white_color] * 13)

# Run the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            column = mouse_x // cell_size
            row = mouse_y // cell_size
            if (cell_size <= mouse_x <= cell_size*12 and
                cell_size <= mouse_y <= cell_size*12 and
                game.get_tile((row, column)) is None):

                game.change_tile((row, column), "A")


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
                pygame.gfxdraw.filled_circle(screen, x, y,
                                             circle_radious, board[i][j])
                pygame.gfxdraw.aacircle(screen, x, y,
                                        circle_radious, board[i][j])

            if (board[i][j] == white_color and
                1<=i<=11 and 1<=j<=11):
                pygame.gfxdraw.filled_circle(screen, x, y,
                                             2, (100,100,100))
                pygame.gfxdraw.aacircle(screen, x, y,
                                             2, (100,100,100))



    pygame.display.update()
pygame.quit()