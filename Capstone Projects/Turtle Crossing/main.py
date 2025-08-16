import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move,'w')


game_is_on = True

while game_is_on:

    time.sleep(0.1)
    screen.update()
    car.new_cars()
    car.move()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            score.gameover()
            game_is_on = False
            
    if player.at_finish_line():
        player.goto_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()