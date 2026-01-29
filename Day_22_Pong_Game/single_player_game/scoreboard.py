from turtle import Turtle


FONT = ('Courier', 30, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 260)
        self.write(self.score, align='center', font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def position(self):
        self.goto(0,250)

    def game_over(self):
        self.clear()
        self.write(f'Game Over! Score: {self.score}', align='center', font=FONT)

