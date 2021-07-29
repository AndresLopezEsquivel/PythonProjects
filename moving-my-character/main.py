# Andrés López Esquivel
# UNAM Aero Design

from turtle import Screen
from character import Character
from scoreboard import Scoreboard
from text_file_manager import TextFileManager

screen = Screen()
screen.setup(width=500, height=700)
screen.title("Actividad Aviónica: Telemetría y Control")
my_character = Character()
my_scoreboard = Scoreboard(x_pos=0, y_pos=250)

amount_of_steps = 0
y_limit_1 = -200
y_limit_2 = 200
x_limit_1 = -200
x_limit_2 = 200


def is_inside_limits(x_cord, y_cord):
    is_character_inside_limits = True
    obeys_x_limits = x_limit_1 < x_cord < x_limit_2
    obeys_y_limits = y_limit_1 < y_cord < y_limit_2

    if not (obeys_x_limits and obeys_y_limits):
        is_character_inside_limits = False

    return is_character_inside_limits


def move_north():
    x_cord = my_character.xcor()
    y_cord = my_character.ycor()

    if is_inside_limits(x_cord=x_cord, y_cord=y_cord):
        my_character.move_north()
        my_scoreboard.add_step()
    else:
        my_character.move_backward()


def move_south():
    x_cord = my_character.xcor()
    y_cord = my_character.ycor()

    if is_inside_limits(x_cord=x_cord, y_cord=y_cord):
        my_character.move_south()
        my_scoreboard.add_step()
    else:
        my_character.move_backward()


def move_east():
    x_cord = my_character.xcor()
    y_cord = my_character.ycor()

    if is_inside_limits(x_cord=x_cord, y_cord=y_cord):
        my_character.move_east()
        my_scoreboard.add_step()
    else:
        my_character.move_backward()


def move_west():
    x_cord = my_character.xcor()
    y_cord = my_character.ycor()

    if is_inside_limits(x_cord=x_cord, y_cord=y_cord):
        my_character.move_west()
        my_scoreboard.add_step()
    else:
        my_character.move_backward()


def save_file():
    text_file_manager = TextFileManager()
    text = f"UNAM Aero Design \nAndrés López Esquivel \nNúmero de pasos: {my_scoreboard.get_amount_of_steps()}"
    text_file_manager.write_text_file(text=text)

screen.onkey(fun=move_north, key="w")
screen.onkey(fun=move_south, key="s")
screen.onkey(fun=move_east, key="d")
screen.onkey(fun=move_west, key="a")
screen.listen()

screen.exitonclick()
save_file()