from turtle import Turtle

FONT = ("Courier", 24, "normal")
CURRENT_LEVEL_POSITION = (-280, 270)
HIGHEST_LEVEL_POSITION = (-100, 270)
GAME_DATA_PATH = "./data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.highest_level_achieved = 0
        with open(GAME_DATA_PATH) as data:
            self.highest_level_achieved = int(data.read())
        self.penup()
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(CURRENT_LEVEL_POSITION)
        self.write(arg=f"LEVEL {self.current_level}", font=FONT)
        self.goto(HIGHEST_LEVEL_POSITION)
        self.write(arg=f"Highest level achieved: {self.highest_level_achieved}", font=FONT)

    def increase_level(self):
        self.current_level += 1
        if self.current_level > self.highest_level_achieved:
            with open(GAME_DATA_PATH, "w") as data:
                self.highest_level_achieved = self.current_level
                data.write(f"{self.highest_level_achieved}")
        self.update_level()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)