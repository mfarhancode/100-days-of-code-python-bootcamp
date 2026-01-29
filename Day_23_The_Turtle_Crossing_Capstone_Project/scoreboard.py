from turtle import Turtle


FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-280, 250)
        self.write(f'Level: {self.level}', align='left', font=FONT)


    def level_up(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def position(self,position):
        self.goto(-200,250)

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over', align='center', font=FONT)
