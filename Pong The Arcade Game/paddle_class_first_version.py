from turtle import Turtle

X_POSITION = 350
Y_POSITIONS = [40, 20, 0, -20, -40]


def create_paddle(x_multiplier):
    x_position = x_multiplier * X_POSITION
    paddle_segments = []
    for y_position in Y_POSITIONS:
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.setpos(x_position, y_position)
        paddle_segments.append(new_segment)
    return paddle_segments


class Paddle:

    def __init__(self, paddle_location):
        x_multiplier = 1
        if paddle_location.lower() == "left":
            x_multiplier = -1
        self.segments = create_paddle(x_multiplier=x_multiplier)

    def move_up(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            y_position = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].sety(y_position)
        self.segments[0].sety(self.segments[0].ycor() + 20)

    def move_down(self):
        for segment_index in range(len(self.segments) - 1):
            y_position = self.segments[segment_index + 1].ycor()
            self.segments[segment_index].sety(y_position)
        last_segment = self.segments[len(self.segments) - 1]
        last_segment.sety(last_segment.ycor() - 20)