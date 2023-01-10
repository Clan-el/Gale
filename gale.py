from logic import Game
from interface import Interface


if __name__ == "__main__":
    game = Game()
    # stages = ("starting", "running", "over", "exit", "AI-Eeasy", "AI-Hard")
    stage = "starting"
    interface = Interface(game)

    while stage != "exit":
        stage = interface.choose_mode(stage) if stage == "starting" else stage
        stage = interface.two_players(stage) if stage == "2_players" else stage
        stage = interface.ai_easy(stage) if stage == "AI-Easy" else stage
        # ai hard
        stage = interface.over(stage) if stage == "over" else stage

    interface.close()
