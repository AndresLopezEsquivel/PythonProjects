from turtle import Turtle, Screen
from random import choice, randint


def color_generator():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


colors = ["light steel blue", "sky blue", "dark cyan", "medium spring green", "gold"]
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("blue")
my_screen = Screen()
my_screen.colormode(255)

# for i in range(3, 8):
#     my_turtle.pencolor(choice(colors))
#     degrees_to_rotate = 0
#     degrees_to_rotate = 360 / i
#     distance_to_move = 100
#
#     for number_of_sides in range(i):
#         my_turtle.forward(distance_to_move)
#         my_turtle.right(degrees_to_rotate)

# degrees = [90, 180, 270]
#
# my_turtle.speed(0)
# for i in range(100):
#     my_turtle.forward(10)
#     my_turtle.setheading(choice(degrees))
#     my_turtle.pencolor(color_generator())
#     my_turtle.width(i / 10)

my_turtle.speed(0)
for degrees in range(0, 361):
    my_turtle.setheading(degrees)
    my_turtle.circle(100)
    my_turtle.pencolor(color_generator())

my_screen.exitonclick()
