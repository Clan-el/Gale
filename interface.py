import pygame
import pygame.gfxdraw
from grid import Grid


def draw_text(surf: pygame.surface.Surface, text: str,
              size: int, x: int, y: int):
    """
    Draws text on the surface

    surf : pygame.surface.Surface
        surface of display
    text : str
        text to draw
    size : int
        size of the font
    x : int
        x coordinate
    y : int
        y coordinate
    """

    font_name = pygame.font.match_font("arial")
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)

    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)


# Set the sizes
screen_width, screen_height = 670, 670
cell_size = 50
circle_radious = 23
LEFT = 1  # for the left button of the mouse

# Set the colors for the cells
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (100, 100, 100)
light_grey = (190, 190, 190)


class Interface:
    def __init__(self) -> None:
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption("Shannon switching - Gale")
        self.screen = pygame.display.set_mode((screen_width, screen_height), 0)
        self.screen.fill(white)

    def set_grid(self, grid: Grid):
        self.grid = grid
        self.board = self.clear_board()

    def change_caption(self, new_text):
        text = "Shannon switching - Gale - "
        pygame.display.set_caption(str(text + new_text))

    def draw_board(self, board) -> None:
        for i in range(self.grid.size):
            for j in range(self.grid.size):
                if self.grid.get_cell((i, j)) == self.grid.player1:
                    board[i][j] = red
                elif self.grid.get_cell((i, j)) == self.grid.player2:
                    board[i][j] = blue

                shift = (screen_width - cell_size * self.grid.size)//2
                x = j * cell_size + circle_radious + shift
                y = i * cell_size + circle_radious + shift

                arguments = self.screen, x, y, circle_radious, board[i][j]
                pygame.gfxdraw.filled_circle(*arguments)
                pygame.gfxdraw.aacircle(*arguments)

                if (board[i][j] == white and 1 <= i <= self.grid.size - 2
                   and 1 <= j <= self.grid.size - 2):
                    pygame.gfxdraw.filled_circle(self.screen, x, y, 2, grey)
                    pygame.gfxdraw.aacircle(self.screen, x, y, 2, grey)
        pygame.display.update()

    def clear_board(self) -> list[list[str | None]]:
        board = []
        for _ in range(self.grid.size):
            board.append([white] * self.grid.size)
        return board

    def draw_box(self, rect_width: int, rect_height: int):
        """
        Draw box for the message that is centered on the screen

        rect_width: int

        rect_height: int
        """
        rect_x = (screen_width - rect_width) // 2
        rect_y = (screen_height - rect_height) // 2
        rectangle = (rect_x, rect_y, rect_width, rect_height)
        param = self.screen, light_grey, rectangle, 0, 20
        pygame.draw.rect(*param)
        param = self.screen, black, rectangle, 5, 20
        pygame.draw.rect(*param)

    def choose_mode(self) -> str:
        """
        Displays the options of the mode to choose and waits for the decision
        """
        pygame.display.set_caption("Shannon switching - Gale")
        self.screen.fill(white)
        self.draw_box(300, 300)
        text = "Witaj w GALE!"
        draw_text(self.screen, text, 30, screen_width//2, screen_height//2-200)
        text = "Wybierz tryb gry:"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2-120)
        text = "by Radosław Ślepowroński"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2+300)

        rect_width, rect_height = 210, 45
        rect_x = (screen_width - rect_width) // 2
        rect_y = (screen_height - rect_height) // 2 + 2
        rectangle = (rect_x, rect_y, rect_width, rect_height)

        Button1 = Button(self.screen, "2 Graczy", rectangle, -70)
        Button2 = Button(self.screen, "vs Komputer - Łatwy", rectangle, -10)
        Button3 = Button(self.screen, "vs Komputer - Trudny", rectangle, +50)
        Button4 = Button(self.screen, "AI vs AI", rectangle, +110)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif (event.type == pygame.MOUSEBUTTONDOWN
                      and event.button == LEFT):

                    if Button1.inside(pygame.mouse.get_pos()):
                        return "2_players"
                    elif Button2.inside(pygame.mouse.get_pos()):
                        return "AI-Easy"
                    elif Button3.inside(pygame.mouse.get_pos()):
                        return "AI-Hard"
                    elif Button4.inside(pygame.mouse.get_pos()):
                        return "AI-AI"

            Button1.above(pygame.mouse.get_pos())
            Button2.above(pygame.mouse.get_pos())
            Button3.above(pygame.mouse.get_pos())
            Button4.above(pygame.mouse.get_pos())

    def choose_size(self) -> int:
        """
        Displays the options of the size to choose and waits for the decision
        """
        self.screen.fill(white)
        self.draw_box(300, 300)
        text = "Witaj w GALE!"
        draw_text(self.screen, text, 30, screen_width//2, screen_height//2-200)
        text = "Wybierz rozmiar planszy:"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2-120)
        text = "by Radosław Ślepowroński"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2+300)

        rect_width, rect_height = 210, 45
        rect_x = (screen_width - rect_width) // 2
        rect_y = (screen_height - rect_height) // 2 + 2
        rectangle = (rect_x, rect_y, rect_width, rect_height)

        Button1 = Button(self.screen, "7x7", rectangle, -70)
        Button2 = Button(self.screen, "9x9", rectangle, -10)
        Button3 = Button(self.screen, "11x11", rectangle, +50)
        Button4 = Button(self.screen, "13x13", rectangle, +110)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif (event.type == pygame.MOUSEBUTTONDOWN
                      and event.button == LEFT):

                    if Button1.inside(pygame.mouse.get_pos()):
                        return 7
                    elif Button2.inside(pygame.mouse.get_pos()):
                        return 9
                    elif Button3.inside(pygame.mouse.get_pos()):
                        return 11
                    elif Button4.inside(pygame.mouse.get_pos()):
                        return 13

            Button1.above(pygame.mouse.get_pos())
            Button2.above(pygame.mouse.get_pos())
            Button3.above(pygame.mouse.get_pos())
            Button4.above(pygame.mouse.get_pos())

    def clear_screen(self):
        """
        Makes screen white and prepares for the next round
        """
        self.screen.fill(white)
        self.board = self.clear_board()

    def get_click(self) -> tuple[int, int]:
        """
        Waits for player mouse click to cecide which cell was clicked
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif (event.type == pygame.MOUSEBUTTONDOWN
                      and event.button == LEFT):

                    shift = (screen_width - cell_size * self.grid.size)//2
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = (mouse_x - shift) // cell_size
                    row = (mouse_y - shift) // cell_size
                    first_strip = cell_size + shift
                    last_strip = cell_size * self.grid.size - 1 + shift

                    if (first_strip < mouse_x < last_strip and
                       first_strip < mouse_y < last_strip and
                       self.grid.get_cell((row, column)) is None):

                        return (row, column)

    def over(self, winner: str):
        """
        Displays the victory announcement and waits for decision about closing
        or playing again

        winner : str
            player that has won the game
        """
        pygame.time.delay(200)
        self.draw_box(350, 110)
        condition = winner == self.grid.player1
        winner = "Czerwony" if condition else "Niebieski"
        text = f"Wygrał gracz {winner}"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2-15)
        text = "Kliknij, aby zagrać ponownie lub wyjdź"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2+15)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return

    def wait_for_closing(self):
        """
        Waits for closing the window
        """
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def check_for_closing(self):
        """
        Waits for closing the window
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


class Button:
    def __init__(self, screen: pygame.surface.Surface, text: str,
                 rectangle: tuple[int, int, int, int], offset: int):

        """
        Initializes the button parameters that are in the middle
        of the horizontal dimension of the screen and leveled by offset

        screen : pygame.surface.Surface
            surface of the display
        text : str
            text that will be shown on the button
        rectangle : tuple[int, int, int, int]
            sizes of the button
        offset : int
            vertical offset of the button
        """
        rect_x, rect_y, rect_width, rect_height = rectangle
        rect_y += offset
        self.rectangle = rect_x, rect_y, rect_width, rect_height
        self.screen = screen
        self.text = text
        self.offset = offset

        self.draw_button(white)

    def draw_button(self, color: tuple[int, int, int]):
        """
        Draws an inactive button

        color : tuple[int, int, int]
            color of the inside of the button
        """
        pygame.draw.rect(self.screen, color, self.rectangle, 0, 20)
        self.area = pygame.draw.rect(self.screen, black, self.rectangle, 2, 20)
        draw_text(self.screen, self.text, 18, screen_width//2,
                  screen_height//2+self.offset)
        pygame.display.update()

    def inside(self, mouse: tuple[int, int]) -> bool:
        """
        Checks if mouse click was in the button and colors clicked button

        mouse : tuple[int, int]
            co-ordinates of the mouse
        """
        if self.area.collidepoint(mouse):
            self.draw_button(blue)
            pygame.time.delay(333)
            return True
        return False

    def above(self, mouse: tuple[int, int]):
        """
        Changes the button color if mouse is above the button

        mouse : tuple[int, int]
            co-ordinates of the mouse
        """
        if self.area.collidepoint(mouse):
            self.draw_button(red)
        else:
            self.draw_button(white)
