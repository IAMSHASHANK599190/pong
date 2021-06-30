from turtle import Turtle, Screen
from recbars import *
from score import *

screen = Screen()
screen.setup(width=850, height=850)
screen.bgcolor("black")
number = Newscore()
number2 = Newscore2()

bar = Recbar()
bar2 = Recbar2()

center_line = Turtle()
center_line.color("white")
center_line.width(5)
center_line.speed("fastest")
center_line.hideturtle()
center_line.penup()
center_line.goto(0, 425)
center_line.setheading(-90)

number.newscore()
number2.newscore()

code = True

while code:
    center_line.pendown()
    center_line.forward(10)
    center_line.penup()
    center_line.forward(10)

screen.exitonclick()
