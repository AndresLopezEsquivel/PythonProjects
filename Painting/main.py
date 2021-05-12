# Andrés López Esquivel
# 05/11/2021
# Project: Hirst Spot Painting

from turtle import Turtle, Screen
import colorgram as cg
import random


def get_colors_from_image(image_name, number_of_colors):
    rgb_list = []
    colors_extracted = cg.extract(image_name, number_of_colors)
    for index in range(len(colors_extracted)):
        r = colors_extracted[index].rgb.r
        g = colors_extracted[index].rgb.b
        b = colors_extracted[index].rgb.b
        rgb_list.append((r, g, b))
    return rgb_list


colors_list = get_colors_from_image("spot_painting.jpg", 5)
my_turtle = Turtle()
my_screen = Screen()
my_screen.colormode(255)
y_position = 0
my_turtle.hideturtle()

for row in range(6):
    for column in range(5):
        print(my_turtle.position())
        random_color = random.choice(colors_list)
        my_turtle.dot(20, random_color)
        my_turtle.penup()
        my_turtle.forward(50)
        my_turtle.pendown()
    y_position += 50
    my_turtle.penup()
    my_turtle.setpos(0, y_position)
    my_turtle.pendown()

my_screen.exitonclick()