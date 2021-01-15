from turtle import Turtle


class Snake:

    def __init__(self):
        self.segments = []
        for i in range(3):
            snake_square = Turtle("square")
            snake_square.color("White")
            snake_square.penup()
            snake_square.goto((-20 * i), 0)
            self.segments.append(snake_square)
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)