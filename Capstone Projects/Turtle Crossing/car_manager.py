from turtle import Turtle, colormode
from random import choice, randint

RGB_COLORS  = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
colormode(255)


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = range(-250,250,20)
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager:
    
    def __init__(self):
        self.all_cars = []
        self.cars_speed = STARTING_MOVE_DISTANCE

    def new_cars(self):

        if randint(1,6) == 1:
            new_car = Turtle('square')
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(choice(RGB_COLORS))
            new_car.goto(300,choice(POSITIONS))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.cars_speed)

    def level_up(self):
        self.cars_speed += MOVE_INCREMENT