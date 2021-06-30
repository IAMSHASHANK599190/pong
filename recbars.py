from turtle import Turtle,Screen
screen=Screen()
screen.bgcolor("black")
class Recbar(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4,stretch_wid=1)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(-370,0)
        self.setheading(90)
class Recbar2(Turtle):
    def __init__(self):

        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=4,stretch_wid=1)
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.penup()
        self.goto(370,0)
        self.setheading(90)



