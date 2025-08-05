from turtle import Turtle, Screen
from random import choice

tota = Turtle()
tota.shape('classic')


colors = ["red", "green", "blue", "orange", "purple", "brown", "pink"]
num = 0
for sides in range(3,10):
    tota.color(colors[num])
    num += 1
    for x in range(sides):
        angle = 360 / sides
        tota.forward(100)
        tota.right(angle)

screen = Screen()
screen.exitonclick()

