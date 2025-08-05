from turtle import Turtle, Screen
from random import choice

tota = Turtle()
tota.shape('classic')

for x in range(11):
    tota.forward(10)
    tota.penup()
    tota.forward(10)
    tota.pendown()

screen = Screen()
screen.exitonclick()

