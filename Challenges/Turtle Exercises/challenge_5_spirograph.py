from turtle import Turtle, Screen
from random import randint
import turtle

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    tup = (r,g,b)

    return tup

turtle.colormode(255)

tota = Turtle()
tota.shape('classic')
tota.pensize(1)
tota.speed(0)


for x in range(int(360/5)): #To stop at beginning
    tota.pencolor(random_color())
    tota.circle(100)
    tota.left(5)



screen = Screen()
screen.exitonclick()

