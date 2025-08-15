from turtle import Turtle, circle

class Ball(Turtle):
     def __init__(self, shape = "circle", undobuffersize = 1000, visible = True):
          super().__init__(shape, undobuffersize, visible)
          self.color('white')
          self.penup()
          self.speed(1)
          self.move_x = 10
          self.move_y = 10

     def move(self):
          new_x = self.xcor() + self.move_x
          new_y = self.ycor() + self.move_y
          
          self.goto(new_x,new_y)

     def bounce_y(self):
          self.move_y *= -1

     def bounce_x(self):
          self.move_x *= -1

     def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()