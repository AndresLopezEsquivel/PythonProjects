# Andrés López Esquivel
# 05/12/2021
# Project: Etch A Sketch

from turtle import Turtle, Screen

my_turtle = Turtle()
my_screen = Screen()


def move_forward():
    my_turtle.forward(10)


def move_backward():
    my_turtle.backward(10)


def rotate_counter_clockwise():
    my_turtle.setheading(my_turtle.heading() + 10)


def rotate_clockwise():
    my_turtle.setheading(my_turtle.heading() - 10)


my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_backward, key="s")
my_screen.onkey(fun=rotate_counter_clockwise, key="a")
my_screen.onkey(fun=rotate_clockwise, key="d")
my_screen.onkey(fun=my_turtle.reset, key="c")
my_screen.listen()
my_screen.exitonclick()
