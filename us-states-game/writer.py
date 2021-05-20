from turtle import Turtle

ALIGNMENT = "center"


class Writer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def write_state_name(self, state_name, coordinates):
        self.goto(coordinates)
        self.write(arg=state_name, align="center")
        self.home()
