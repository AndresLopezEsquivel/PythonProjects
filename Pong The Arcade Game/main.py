from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
game_continues = True

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong: The Arcade Game")
screen.tracer(0)

left_paddle = Paddle(paddle_position=(-350, 0))
right_paddle = Paddle(paddle_position=(350, 0))

screen.update()

screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")

screen.listen()

while game_continues:
    screen.update()
    time.sleep(0.05)

screen.exitonclick()
