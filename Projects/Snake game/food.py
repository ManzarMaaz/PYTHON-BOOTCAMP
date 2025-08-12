import random
from turtle import Turtle, penup



class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("apple_small.gif")
        self.shapesize(0.5,0.5)
        self.penup()
        self.refresh()


    def refresh(self):
        x = random.randint(-270,270)
        y = random.randint(-270,250)
        self.goto(x,y)
