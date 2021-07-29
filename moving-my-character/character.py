from turtle import Turtle

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180
AMOUNT_OF_MOVEMENT = 10


class Character(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.setheading(NORTH)
        self.penup()
        self.shape("turtle")
        self.showturtle()

    def move_north(self):
        self.setheading(NORTH)
        self.forward(AMOUNT_OF_MOVEMENT)

    def move_south(self):
        self.setheading(SOUTH)
        self.forward(AMOUNT_OF_MOVEMENT)

    def move_east(self):
        self.setheading(EAST)
        self.forward(AMOUNT_OF_MOVEMENT)

    def move_west(self):
        self.setheading(WEST)
        self.forward(AMOUNT_OF_MOVEMENT)

    def move_backward(self):
        self.backward(10)
