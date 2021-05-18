from random import randint
from turtle import Turtle

DISTANCE = 10


def generate_random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def create_obstacle(x_position, y_position):
    new_obstacle = Turtle()
    new_obstacle.shape("square")
    new_obstacle.shapesize(stretch_wid=1.0, stretch_len=2.0)
    new_obstacle.color(generate_random_color())
    new_obstacle.penup()
    new_obstacle.setpos(x_position, y_position)
    new_obstacle.setheading(180)
    return new_obstacle


class Obstacles:

    def __init__(self, y_limits, x_limits):
        self.speed_value = 0.1
        self.y_limits = y_limits
        self.x_limits = x_limits
        self.obstacles_list = []
        self.obstacles_list.append(create_obstacle(self.x_limits[1], self.y_limits[1]))

    def generate_obstacles(self):
        random_choice = randint(1, 6)
        if random_choice == 2:
            x_position = self.x_limits[1]
            y_position = randint(self.y_limits[0], self.y_limits[1])
            new_obstacle = create_obstacle(x_position, y_position)
            self.obstacles_list.append(new_obstacle)
        self.move_obstacles()

    def move_obstacles(self):
        for obstacle in self.obstacles_list:
            obstacle.forward(DISTANCE)
            if obstacle.xcor() < self.x_limits[0]:
                obstacle.hideturtle()
                self.obstacles_list.remove(obstacle)

    def increase_speed(self):
        self.speed_value *= 0.9
