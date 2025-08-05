from turtle import Turtle, Screen
from random import choice

tota = Turtle()
tota.shape('classic')

# for x in range(4):
#     tota.forward(100)
#     tota.right(90)

# tota.forward(100)
# tota.right(90)

# tota.forward(100)
# tota.right(90)

# tota.forward(100)
# tota.right(90)

# for x in range(11):
#     tota.forward(10)
#     tota.penup()
#     tota.forward(10)
#     tota.pendown()


# tota.color('violet')
# for x in range(3):
#     tota.forward(100)
#     tota.right(120)

# tota.color('indigo')
# for x in range(4):
#     tota.forward(100)
#     tota.right(90)

# tota.color('blue')
# for x in range(5):
#     tota.forward(100)
#     tota.right(72)

# tota.color('green')
# for x in range(6):
#     tota.forward(100)
#     tota.right(60)

# tota.color('yellow')
# for x in range(7):
#     tota.forward(100)
#     tota.right(51.43)

# tota.color('orange')
# for x in range(8):
#     tota.forward(100)
#     tota.right(45)

# tota.color('red')
# for x in range(9):
#     tota.forward(100)
#     tota.right(40)

# tota.color('brown')
# for x in range(10):
#     tota.forward(100)
#     tota.right(36)
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

