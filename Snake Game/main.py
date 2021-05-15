from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
game_continues = True

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

screen.onkey(fun=snake.move_up, key="Up")
screen.onkey(fun=snake.move_down, key="Down")
screen.onkey(fun=snake.move_right, key="Right")
screen.onkey(fun=snake.move_left, key="Left")
screen.listen()

while game_continues:

    x = snake.head.xcor()
    y = snake.head.ycor()

    screen.update()
    time.sleep(0.09)
    snake.move()

    if snake.head.distance(food) < 15:
        food.change_location()
        scoreboard.add_point()
        snake.extend()

    if x < -280 or x > 280 or y < -280 or y > 280:
        game_continues = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_continues = False
                scoreboard.game_over()

screen.exitonclick()