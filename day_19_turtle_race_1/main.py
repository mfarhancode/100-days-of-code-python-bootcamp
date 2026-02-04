from turtle import Turtle, Screen, TK
from random import randint
import sys


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
FINISH_LINE_X = SCREEN_WIDTH//2 - 80
print(FINISH_LINE_X)

s = Screen()
s.title('Turtle Race')
s.bgcolor('black')
s.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

colors = ['blue', 'green', 'red', 'yellow', 'purple', 'gray']

turtles = []
for color in colors:
    t = Turtle('turtle')
    t.hideturtle()
    t.color(color)
    turtles.append(t)

all_colors = ', '.join(colors)
# print(f'The available turtle colors are: {all_colors}')
while True:
    user_bet = s.textinput(title='Make your bet', 
        prompt='Which turtle will win the race? The available turtle colors are:\n' + all_colors + '\nEnter a color: ')
    if user_bet is None:
        TK.messagebox.showinfo(title="Turtle Race", message="Game exited. Goodbye!")
        sys.exit()
    user_bet = user_bet.strip().lower()
    if user_bet in colors:
        # print(user_bet)
        break
    TK.messagebox.showwarning(
    title="Invalid Input",
    message="Please choose a color from given colors list.")


# draw a line
line = Turtle()
line.hideturtle()
line.penup()
line.goto(240,200)
line.pendown()
line.color('white')
line.pensize(3)
line.right(90)
line.forward(400)

# set positions
start_x, start_y = -280, 150
for t in turtles:
    t.penup()
    t.goto(start_x, start_y)
    t.showturtle()
    start_y -= 50
    # print(t.color())

game_on = True
while game_on:
    for t in turtles:
        t.forward(randint(1,10))

         # check the position of turtles after each step
        # check if any turtle reach end line
        if t.xcor() >= FINISH_LINE_X:
            winner_color = t.pencolor()
            game_on = False

# print message who won
message = ''

if winner_color == user_bet:
    message = f'Congratulations!! The {winner_color} turtle has won.'
else:
    message = f'The winner is {winner_color} turtle. Try again next time.'

TK.messagebox.showinfo(title="Turtle Race", message=message)
s.mainloop()