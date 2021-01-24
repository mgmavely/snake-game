from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("save_data.txt", mode="r") as save_data:
    contents = save_data.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        if contents != '':
            self.high_score = int(contents)
        else:
            self.high_score = 0
        self.pencolor("white")
        self.penup()
        self.goto(-10, 265)

    def score_check(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def point(self):
        self.score += 1
        self.score_check()

    def rst(self):
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("save_data.txt", mode="w") as save_data:
                save_data.write(str(self.high_score))
        self.score = 0
        self.score_check()
