from turtle import Turtle, Screen, ycor
import turtle
import random

screen = Screen()
screen.setup(500,400)

turtles = []
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
x = -230
y = [150,100,50,0,-50,-100]

for turtle in range(0,6):
    tim = Turtle(shape='turtle')
    tim.color(colors[turtle])
    tim.penup()
    tim.goto(x,y[turtle])
    turtles.append(tim)
    

user_choice = screen.textinput(title='Guess the Winner', prompt="Choose only from 'red', 'green', 'blue', 'yellow', 'orange', 'purple' : ")

if user_choice.lower() in colors:
    race = True
else:
    print('Invalid Input')

winner = None
finish_line = 230

while race:
    current_turtle = random.choice(turtles)
    current_turtle.forward(random.randint(1,10))

    for t in turtles:
        if t.xcor() >= finish_line:
            winner = t
            race = False
            break
        

if user_choice.lower() == winner.pencolor():
    screen.title(f'You Won !!! The Winner is {winner.pencolor().title()} Turtle')
    screen.bgcolor('GreenYellow')
else:
    screen.title(f'You Lost !!! The Winner is {winner.pencolor().title()} Turtle')
    screen.bgcolor('IndianRed1')


screen.exitonclick()
