import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from obstacles import Obstacles

game_continues = True

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.colormode(255)

player = Player()
scoreboard = Scoreboard()
obstacles = Obstacles(y_limits=(-240, 250), x_limits=(-310, 310))

screen.onkey(fun=player.move, key="Up")
screen.listen()

while game_continues:
    time.sleep(obstacles.speed_value)
    screen.update()
    obstacles.generate_obstacles()

    if player.ycor() >= 280:
        player.go_to_origin()
        scoreboard.increase_level()
        obstacles.increase_speed()

    for obstacle in obstacles.obstacles_list:
        if player.distance(obstacle) < 15:
            scoreboard.game_over()
            game_continues = False

screen.exitonclick()