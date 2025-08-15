from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

import time

screen = Screen()
screen.setup(800,600)
screen.title('Pong Py')
screen.bgcolor('black')

screen.tracer(0)

l_paddle = Paddle((-380,0))
r_paddle = Paddle((370,0))

score = Scoreboard()
ball = Ball()

line = Turtle('square')
line.color('white')
line.penup()
line.goto(0,300)
line.setheading(270)

while line.ycor() > -300:
    line.pendown()
    line.forward(1)
    line.penup()

screen.listen()
screen.onkey(l_paddle.up,'w')
screen.onkey(l_paddle.down,'s')
screen.onkey(r_paddle.up,'Up')
screen.onkey(r_paddle.down,'Down')

game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # Right paddle collision
    elif ball.xcor() > 350 and ball.distance(r_paddle) < 50:
        ball.bounce_x()
        print("bounce right")

    # Left paddle collision
    elif ball.xcor() < -350 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        print("bounce left")
        
     # Detect if ball goes out of bounds
    if ball.xcor() > 380:
        score.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        score.r_point()
        ball.reset_position()

screen.exitonclick()