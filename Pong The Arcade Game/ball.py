from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_increment = 5
        self.y_increment = 5
        self.value_of_speed = 0.1

    def move(self):
        x_position = self.xcor() + self.x_increment
        y_position = self.ycor() + self.y_increment
        self.goto(x_position, y_position)

    def bounce_vertically(self):
        self.y_increment *= -1

    def bounce_horizontally(self):
        self.x_increment *= -1
        self.value_of_speed *= 0.6

    def reset(self):
        self.home()
        self.bounce_horizontally()