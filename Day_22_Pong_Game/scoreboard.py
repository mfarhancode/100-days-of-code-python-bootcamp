from turtle import Turtle


FONT = ('Courier', 30, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 260)
        self.write(self.l_score, align='left', font=FONT)
        self.goto(100, 260)
        self.write(self.r_score, align='right', font=FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()


    def position(self,position):
        self.goto(0,250)
