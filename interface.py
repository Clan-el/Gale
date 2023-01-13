import pygame
import pygame.gfxdraw
from bot import easy_bot_move
from logic import Game


def draw_text(surf: pygame.surface.Surface, text: str,
              size: int, x: int, y: int):

    font_name = pygame.font.match_font("arial")
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)

    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surf.blit(text_surface, text_rect)


# Set the sizes
screen_width, screen_height = 670, 670
offset = 10
cell_size = 50
circle_radious = 23
LEFT = 1

# Set the colors for the cells
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
grey = (100, 100, 100)
light_grey = (190, 190, 190)


class Interface:
    def __init__(self, game: Game) -> None:
        pygame.display.init()
        pygame.font.init()
        pygame.display.set_caption("Shannon switching - Gale")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill(white)
        self.game = game
        self.board = self.clear_board()

    def draw_board(self, board) -> None:
        for i in range(self.game.size):
            for j in range(self.game.size):
                if self.game.grid.get_cell((i, j)) == self.game.player1:
                    board[i][j] = red
                elif self.game.grid.get_cell((i, j)) == self.game.player2:
                    board[i][j] = blue

                x = j * cell_size + circle_radious + offset
                y = i * cell_size + circle_radious + offset

                arguments = self.screen, x, y, circle_radious, board[i][j]
                pygame.gfxdraw.filled_circle(*arguments)
                pygame.gfxdraw.aacircle(*arguments)

                if (board[i][j] == white and 1 <= i <= self.game.size - 2
                   and 1 <= j <= self.game.size - 2):
                    pygame.gfxdraw.filled_circle(self.screen, x, y, 2, grey)
                    pygame.gfxdraw.aacircle(self.screen, x, y, 2, grey)
        pygame.display.update()

    def clear_board(self) -> list[list[str | None]]:
        board = []
        for _ in range(self.game.size):
            board.append([white] * self.game.size)
        return board

    def endgame_box(self) -> None:
        self.draw_box(350, 110)
        condition = self.game.check_win() == self.game.player1
        winner = "Czerwony" if condition else "Niebieski"
        text = f"Wygrał gracz {winner}"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2-15)
        text = "Kliknij, aby zagrać ponownie lub wyjdź"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2+15)

    def draw_box(self, rect_width: int, rect_height: int) -> None:
        rect_x = (screen_width - rect_width) // 2
        rect_y = (screen_height - rect_height) // 2
        rectangle = (rect_x, rect_y, rect_width, rect_height)
        param = self.screen, light_grey, rectangle, 0, 20
        pygame.draw.rect(*param)
        param = self.screen, black, rectangle, 5, 20
        pygame.draw.rect(*param)

    def choose_mode(self, stage: str) -> str:
        self.screen.fill(white)
        self.draw_box(300, 300)
        text = "Witaj w GALE!"
        draw_text(self.screen, text, 30, screen_width//2, screen_height//2-200)
        text = "Wybierz tryb gry:"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2-100)
        text = "by Radosław Ślepowroński"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2+300)

        rect_width, rect_height = 210, 45
        rect_x = (screen_width - rect_width) // 2
        rect_y = (screen_height - rect_height) // 2 + 2
        rectangle = (rect_x, rect_y, rect_width, rect_height)

        Button1 = Button(self.screen, "2 Graczy", rectangle, -40)
        Button2 = Button(self.screen, "vs Komputer - Łatwy", rectangle, +30)
        Button3 = Button(self.screen, "vs Komputer - Trudny", rectangle, +100)
        pygame.display.flip()

        while stage == "starting":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"

                elif (event.type == pygame.MOUSEBUTTONDOWN
                      and event.button == LEFT):

                    if Button1.inside(pygame.mouse.get_pos()):
                        return "2_players"
                    elif Button2.inside(pygame.mouse.get_pos()):
                        return "AI-Easy"
                    elif Button3.inside(pygame.mouse.get_pos()):
                        # return "AI-Hard"
                        pass

            Button1.above(pygame.mouse.get_pos())
            Button2.above(pygame.mouse.get_pos())
            Button3.above(pygame.mouse.get_pos())

        return "exit"

    def two_players(self, stage: str) -> str:
        self.screen.fill(white)
        board = self.clear_board()
        moves = 0
        while stage == "2_players":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage = "exit"

                elif (event.type == pygame.MOUSEBUTTONDOWN
                      and event.button == LEFT):
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = (mouse_x - offset) // cell_size
                    row = (mouse_y - offset) // cell_size
                    first_strip = cell_size + offset
                    last_strip = cell_size * self.game.size - 1 + offset

                    if (first_strip < mouse_x < last_strip and
                       first_strip < mouse_y < last_strip and
                       self.game.grid.get_cell((row, column)) is None):

                        moves += 1
                        if moves % 2 == 1:
                            self.game.grid.change_cell((row, column),
                                                       self.game.player1)
                        else:
                            self.game.grid.change_cell((row, column),
                                                       self.game.player2)

            self.draw_board(board)

            if self.game.check_win():
                return "over"

        return "exit"

    def ai_easy(self, stage: str) -> str:
        self.screen.fill(white)
        board = self.clear_board()
        self.draw_board(board)
        # moves = 0
        while stage == "AI-Easy":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage = "exit"

                elif (event.type == pygame.MOUSEBUTTONDOWN and
                      event.button == LEFT):

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = (mouse_x - offset) // cell_size
                    row = (mouse_y - offset) // cell_size
                    first_strip = cell_size + offset
                    last_strip = cell_size*self.game.size - 1 + offset

                    if (first_strip < mouse_x < last_strip and
                       first_strip < mouse_y < last_strip and
                       self.game.grid.get_cell((row, column)) is None):

                        self.game.grid.change_cell((row, column),
                                                   self.game.player1)
                        self.draw_board(board)

                        if self.game.check_win():
                            return "over"

                        pygame.time.delay(1000)
                        cell_cords = easy_bot_move(self.game.grid)
                        self.game.grid.change_cell(cell_cords,
                                                   self.game.player2)
                        self.draw_board(board)

                        if self.game.check_win():
                            return "over"

        return "exit"

    def over(self, stage: str) -> str:
        self.endgame_box()
        pygame.display.update()

        while stage == "over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    stage = "exit"

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.grid.clear_grid()
                    return "starting"

        return "exit"

    def close(self):
        pygame.quit()


class Button:
    def __init__(self, screen: pygame.surface.Surface, text: str,
                 rectangle: tuple[int, int, int, int], offset: int):

        rect_x, rect_y, rect_width, rect_height = rectangle
        rect_y += offset
        self.rectangle = rect_x, rect_y, rect_width, rect_height
        self.screen = screen
        self.text = text
        self.offset = offset

        self.draw_button(white)

    def inside(self, mouse: tuple[int, int]) -> bool:
        if self.area.collidepoint(mouse):
            self.draw_button(blue)
            pygame.time.delay(333)
            return True
        return False

    def above(self, mouse: tuple[int, int]) -> None:
        if self.area.collidepoint(mouse):
            self.draw_button(red)
        else:
            self.draw_button(white)

    def draw_button(self, color: tuple[int, int, int]):
        pygame.draw.rect(self.screen, color, self.rectangle, 0, 20)
        self.area = pygame.draw.rect(self.screen, black, self.rectangle, 2, 20)
        draw_text(self.screen, self.text, 18, screen_width//2,
                  screen_height//2+self.offset)
        pygame.display.update()
