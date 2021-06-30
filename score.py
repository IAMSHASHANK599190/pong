from turtle import Turtle, Screen
ALIGN="center"
FONT=("Courier",100,"normal")

class Newscore(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")

        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(-160, 280)

        self.score = 0

    def newscore(self):
        self.write(f" {self.score}",align=ALIGN,font=FONT)
    def scoretrack(self):
        self.score += 1
        self.clear()
        self.newscore()
class Newscore2(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")

        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(60, 280)

        self.score = 0

    def newscore(self):
        self.write(f" {self.score}",align=ALIGN,font=FONT)
    def scoretrack(self):
        self.score += 1
        self.clear()
        self.newscore()
