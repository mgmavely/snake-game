from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.goto(random.randint(-14, 14)*20, random.randint(-14, 12)*20)

    def refresh(self):
        self.goto(random.randint(-14, 14)*20, random.randint(-14, 12)*20)
