from turtle import Turtle

FONT = ("Courier", 30, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.number_of_steps = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(self.x_pos, self.y_pos)
        text_to_show = f"Número de pasos: {self.number_of_steps}"
        self.write(arg=text_to_show, align=ALIGNMENT, font=FONT)

    def add_step(self):
        self.number_of_steps += 1
        self.update_scoreboard()

    def get_amount_of_steps(self):
        return self.number_of_steps
