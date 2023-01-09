import pygame, pygame.gfxdraw
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'

from bot import easy_bot_move

def draw_text(surf, text: str, size: int, x: int, y: int):
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
    def __init__(self, game) -> None:
        pygame.init()
        pygame.display.set_caption("Shannon switching - Gale")
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen.fill(white)
        self.game = game
        self.board = self.clear_board()

    def draw_board(self, board):
        for i in range(13):
            for j in range(13):
                if self.game.get_cell((i, j)) == "C":
                    board[i][j] = red
                elif self.game.get_cell((i, j)) == "N":
                    board[i][j] = blue

                x = j * cell_size + circle_radious + offset
                y = i * cell_size + circle_radious + offset

                arguments = self.screen, x, y, circle_radious, board[i][j]
                pygame.gfxdraw.filled_circle(*arguments)
                pygame.gfxdraw.aacircle(*arguments)

                if (board[i][j] == white and 1<=i<=11 and 1<=j<=11):
                    pygame.gfxdraw.filled_circle(self.screen, x, y, 2, grey)
                    pygame.gfxdraw.aacircle(self.screen, x, y, 2, grey)
        pygame.display.update()


    def clear_board(self) -> list[list[str|None]]:
        board = []
        for _ in range(13):
            board.append([white] * 13)
        return board


    def endgame_box(self):
        self.draw_box(320, 110)

        winner = "Czerwony" if self.game.check_win() == "C" else "Niebieski"
        text = f"Wygrał gracz {winner}"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2-15)
        text = "Kliknij, aby kontynuować lub wyjdź"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2+15)


    def draw_box(self, rect_width: int, rect_height: int):
        rect_x = (screen_width - rect_width) // 2
        rect_y = (screen_height - rect_height) // 2
        rectangle = (rect_x, rect_y, rect_width, rect_height)
        param = self.screen, light_grey, rectangle, 0, 20
        pygame.draw.rect(*param)
        param = self.screen, black, rectangle, 5, 20
        pygame.draw.rect(*param)


    def choose_mode(self, current_stage: str) -> str | None:
        self.screen.fill(white)
        self.draw_box(300, 300)
        text = "Wybierz tryb gry:"
        draw_text(self.screen, text, 18, screen_width//2, screen_height//2-100)

        rect_width, rect_height = 210, 45
        rect_x = (screen_width - rect_width) // 2
        rect_y = (screen_height - rect_height) // 2 + 2
        rectangle = (rect_x, rect_y, rect_width, rect_height)

        Button1 = Button(self.screen, "2 Graczy", rectangle, -40)
        Button2 = Button(self.screen, "vs Komputer - Łatwy", rectangle, +30)
        Button3 = Button(self.screen, "vs Komputer - Trudny", rectangle, +100)
        pygame.display.flip()

        while current_stage == "starting":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    if Button1.inside(pygame.mouse.get_pos()):
                        return "running"
                        # return "2_players"
                    elif Button2.inside(pygame.mouse.get_pos()):
                        return "AI-Easy"
                    elif Button3.inside(pygame.mouse.get_pos()):
                        # return "AI-Hard"
                        pass


    def play(self, current_stage: str) -> str | None:
        self.screen.fill(white)
        board = self.clear_board()
        moves = 0
        while current_stage == "running":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = (mouse_x - offset) // cell_size
                    row = (mouse_y - offset) // cell_size
                    first_strip = cell_size + offset
                    last_strip = cell_size*12 + offset

                    if (first_strip < mouse_x < last_strip and
                        first_strip < mouse_y < last_strip and
                        self.game.get_cell((row, column)) is None):

                        moves += 1
                        if moves % 2 == 1:
                            self.game.change_cell((row, column), "C")
                        else:
                            self.game.change_cell((row, column), "N")

            self.draw_board(board)

            if self.game.check_win():
                return "over"


    def ai_easy(self, current_stage: str) -> str | None:
        self.screen.fill(white)
        board = self.clear_board()
        self.draw_board(board)
        while current_stage == "AI-Easy":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"

                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    column = (mouse_x - offset) // cell_size
                    row = (mouse_y - offset) // cell_size
                    first_strip = cell_size + offset
                    last_strip = cell_size*12 + offset

                    if (first_strip < mouse_x < last_strip and
                        first_strip < mouse_y < last_strip and
                        self.game.get_cell((row, column)) is None):

                        self.game.change_cell((row, column), "C")
                        self.draw_board(board)

                        if self.game.check_win():
                            return "over"

                        pygame.time.delay(1000)
                        cell_cords = easy_bot_move(self.game)
                        self.game.change_cell(cell_cords, "N")
                        self.draw_board(board)

                        if self.game.check_win():
                            return "over"




    def over(self, current_stage: str) -> str | None:
        self.endgame_box()
        pygame.display.update()

        while current_stage == "over":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.game.clear_grid()
                    return "starting"

    def close(self):
        pygame.quit()



class Button:
    def __init__(self, screen, text:str, rectangle:tuple[int,int,int,int], offset:int):
        rect_x, rect_y, rect_width, rect_height = rectangle
        rect_y += offset
        rectangle = rect_x, rect_y, rect_width, rect_height
        pygame.draw.rect(screen, white, rectangle, 0, 20)
        pygame.draw.rect(screen, black, rectangle, 2, 20)

        draw_text(screen, text, 18, screen_width//2, screen_height//2+offset)

        (self._rect_x, self._rect_y, self._rect_width,
        self._rect_height) = rectangle

    def inside(self, mouse: tuple[int, int]) -> bool:
        mouse_x, mouse_y = mouse
        if self._rect_x < mouse_x < self._rect_x + self._rect_width:
            if self._rect_y < mouse_y < self._rect_y + self._rect_height:
                return True
        return False