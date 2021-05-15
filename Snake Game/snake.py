from turtle import Turtle

DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.setpos(position)
        return new_segment

    def create_snake(self):
        x1 = 40.0
        for _ in range(3):
            self.snake.append(self.create_segment((x1, 0)))
            x1 = x1 - DISTANCE

    def extend(self):
        last_position = self.snake[-1].pos()
        new_segment = self.create_segment(last_position)
        self.snake.append(new_segment)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):
        for segment_index in range(len(self.snake) - 1, 0, -1):
            x_pos = self.snake[segment_index - 1].xcor()
            y_pos = self.snake[segment_index - 1].ycor()
            self.snake[segment_index].goto(x_pos, y_pos)
        self.snake[0].forward(DISTANCE)