from turtle import Turtle, Screen, TK
from random import randint
import sys


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
FINISH_LINE_X = SCREEN_WIDTH//2 - 80
START_X, START_Y = -(SCREEN_WIDTH//2-20), SCREEN_HEIGHT//2 -100

COLORS = ['blue', 'green', 'red', 'yellow', 'purple', 'gray']
all_colors = ', '.join(COLORS)

class TurtleRace:
    def __init__(self):
        self.turtles = []
        self.colors = COLORS
        for color in self.colors:
            t = Turtle('turtle')
            t.hideturtle()
            t.color(color)
            self.turtles.append(t)
        self.endline = None
        self.game_on = True
        self.winner = None
        self.start_x = START_X
        self.start_y = START_Y

    def draw_endline(self):
        self.endline = Turtle()
        self.endline.hideturtle()
        self.endline.penup()
        self.endline.goto(FINISH_LINE_X + 20, SCREEN_HEIGHT//2 - 50)
        self.endline.pendown()
        self.endline.color('white')
        self.endline.pensize(3)
        self.endline.right(90)
        self.endline.forward(400)

    def set_positions(self):
        x, y = self.start_x, self.start_y
        for t in self.turtles:
            t.penup()
            t.goto(x, y)
            t.showturtle()
            y -= 50
    
    def move_turtles(self):
        for t in self.turtles:
            t.forward(randint(1,10))
            # check the position of turtles after each step
            if self.check_winner(trtl=t):
                break
            
    def check_winner(self, trtl):
        # check if any turtle reach end line
        if trtl.xcor() >= FINISH_LINE_X:
            self.winner = trtl
            self.game_on = False
            return True
        return False

