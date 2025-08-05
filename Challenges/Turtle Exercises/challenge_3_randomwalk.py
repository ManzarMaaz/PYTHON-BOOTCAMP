from turtle import Turtle, Screen
from random import choice, randint

colours = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

angles = [0,90,180,270]

tota = Turtle()
tota.shape('classic')
tota.pensize(10)
tota.speed(0)


for x in range(300):
    tota.pencolor(choice(colours))
    tota.forward(20)
    tota.setheading(choice(angles))



screen = Screen()
screen.exitonclick()

