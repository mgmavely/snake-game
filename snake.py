from turtle import Turtle
START = [0, -20, -40]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in START:
            self.add_segment((i, 0))

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def lt(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def rt(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def add_segment(self, position):
        snake_square = Turtle("square")
        snake_square.color("White")
        snake_square.penup()
        snake_square.goto(position)
        self.segments.append(snake_square)

    def rst(self):
        for i in self.segments:
            i.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
