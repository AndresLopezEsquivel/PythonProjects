from turtle import Turtle

SCOREBOARD_POSITION = (100, 200)
FONT = ("Courier", 80, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-1 * SCOREBOARD_POSITION[0], SCOREBOARD_POSITION[1])
        self.write(arg=self.left_paddle_score, align=ALIGNMENT, font=FONT)
        self.goto(SCOREBOARD_POSITION[0], SCOREBOARD_POSITION[1])
        self.write(arg=self.right_paddle_score, align=ALIGNMENT, font=FONT)

    def add_point_to_left_paddle(self):
        self.left_paddle_score += 1
        self.update()

    def add_point_to_right_padddle(self):
        self.right_paddle_score += 1
        self.update()