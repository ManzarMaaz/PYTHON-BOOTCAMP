from food import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):
        self.write(f'Current Score : {self.score}', align=ALIGNMENT, font=FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.color('red')
        self.write('GAME OVER !!!', align=ALIGNMENT, font=FONT)
        