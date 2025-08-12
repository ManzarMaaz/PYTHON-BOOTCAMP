import time
from turtle import Screen, bgcolor
import turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

score = 0

screen = Screen()
screen.bgpic('/Users/mohammad/Desktop/100 DAYS OF CODE/DAY 20/grass_ex.gif')# Grass green hex
screen.setup(600,600)
screen.tracer(0)
screen.register_shape("/Users/mohammad/Desktop/100 DAYS OF CODE/DAY 20/apple_small.gif")


screen.title('Py Snake Game')   

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key='w',fun=snake.up)
screen.onkey(key='s',fun=snake.down)
screen.onkey(key='a',fun=snake.left)
screen.onkey(key='d',fun=snake.right)

game = True
while game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        snake.growth()
        food.refresh()
        snake.growth()
        score.increase_score()

    if abs(snake.head.xcor()) > 300 or abs(snake.head.ycor()) > 300:
        score.gameover()
        game = False

    # Tail collision check
    for segment in snake.segments[1:]:  # skip the head
        if snake.head.distance(segment) < 10:
            game = False
            score.gameover()
        

screen.exitonclick()
