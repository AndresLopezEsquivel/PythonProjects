from turtle import Turtle

FONT = ("Courier", 24, "normal")
POSITION = (-280, 270)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.goto(POSITION)
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(arg=f"LEVEL {self.current_level}", font=FONT)

    def increase_level(self):
        self.current_level += 1
        self.update_level()

    def game_over(self):
        self.home()
        self.write(arg="GAME OVER", align="center", font=FONT)