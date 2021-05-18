from turtle import Turtle

INITIAL_POSITION = (0, -280)
GOAL_Y_POSITION = 280
DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.speed("fastest")
        self.go_to_origin()

    def go_to_origin(self):
        self.setpos(INITIAL_POSITION)

    def move(self):
        self.forward(DISTANCE)
