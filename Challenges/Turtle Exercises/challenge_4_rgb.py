from turtle import Turtle, Screen
from random import choice, randint
import turtle

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    tup = (r,g,b)

    return tup

angles = [0,90,180,270]
turtle.colormode(255)

tota = Turtle()
tota.shape('classic')
tota.pensize(10)
tota.speed(0)


for x in range(300):
    
    tota.pencolor(random_color())
    tota.forward(20)
    tota.setheading(choice(angles))



screen = Screen()
screen.exitonclick()