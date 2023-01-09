from logic import Game
from grid import gridB2
from interface import Interface


if __name__ == "__main__":
    game = Game()
    # stages = ("starting", "running", "over", "exit", "AI-Eeasy", "AI-Hard")
    stage = "starting"
    interface = Interface(game)

    while stage != "exit":
        stage = interface.choose_mode(stage) if stage == "starting" else stage
        stage = interface.play(stage) if stage == "running" else stage
        stage = interface.ai_easy(stage) if stage == "AI-Eeasy" else stage
        # ai hard
        stage = interface.over(stage) if stage == "over" else stage

    interface.close()
