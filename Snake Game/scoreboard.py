from turtle import Turtle

ALIGNMENT = "center"
FONT = ("arial", 15, "bold italic")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.text = f"Score: {self.score} points"
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.update_text()

    def update_text(self):
        self.clear()
        self.text = f"Score: {self.score} points"
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.score += 1
        self.update_text()

    def game_over(self):
        self.home()
        self.text = "GAME OVER"
        self.write(arg=self.text, align=ALIGNMENT, font=FONT)
