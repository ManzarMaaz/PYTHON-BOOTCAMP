from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.score = 0

        with open('data.txt',mode='r') as file:
                self.highscore = int(file.read())
    
        self.penup()
        self.goto(0,270)
        self.update_score()

    def update_score(self):

        self.clear()
        self.write(f'Current Score : {self.score} High Score : {self.highscore}', align='center', font=FONT)
        

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_score()



    # def gameover(self):
    #     self.goto(0,0)
    #     self.color('red')
    #     self.write('GAME OVER !!!', align=ALIGNMENT, font=FONT)
        