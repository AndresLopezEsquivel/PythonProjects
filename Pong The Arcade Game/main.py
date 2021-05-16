from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
game_continues = True

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong: The Arcade Game")
screen.tracer(0)

left_paddle = Paddle(paddle_position=(-350, 0))
right_paddle = Paddle(paddle_position=(350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.update()

screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")

screen.listen()

while game_continues:
    screen.update()
    time.sleep(ball.value_of_speed)
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_vertically()

    ball_collide_right_paddle = ball.distance(right_paddle) < 50 and ball.xcor() > 320
    ball_collide_left_paddle = ball.distance(left_paddle) < 50 and ball.xcor() < -320

    if ball_collide_right_paddle or ball_collide_left_paddle:
        ball.bounce_horizontally()

    # When the right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.add_point_to_left_paddle()

    # When the left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset()
        scoreboard.add_point_to_right_padddle()

screen.exitonclick()
