from turtle import Turtle
ALIGN="center"
FONT=("Courier",100,"normal")


class Newscore2(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")

        self.speed("fastest")
        self.penup()
        self.hideturtle()
        self.goto(75, 280)

        self.score = 0

    def newscore(self):
        self.write(f" {self.score}",align=ALIGN,font=FONT)
    def scoretrack(self):
        self.score += 1
        self.clear()
        self.newscore()
number2=Newscore2()
number2.newscore()