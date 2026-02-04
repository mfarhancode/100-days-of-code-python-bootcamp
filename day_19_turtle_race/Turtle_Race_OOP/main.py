from turtle import Screen, TK
from random import randint
import sys

from turtle_race import TurtleRace


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
FINISH_LINE_X = SCREEN_WIDTH//2 - 80

s = Screen()
s.title('Turtle Race')
s.bgcolor('black')
s.setup(SCREEN_WIDTH,SCREEN_HEIGHT)

turtle_race = TurtleRace()

# print(f'The available turtle colors are: {all_colors}')
while True:
    user_bet = s.textinput(title='Make your bet', 
        prompt='Which turtle will win the race? The available turtle colors are:\n' + ', '.join(turtle_race.colors) + '\nEnter a color: ')
    if user_bet is None:
        TK.messagebox.showinfo(title="Turtle Race", message="Game exited. Goodbye!")
        sys.exit()
    user_bet = user_bet.strip().lower()
    if user_bet in turtle_race.colors:
        # print(user_bet)
        break
    TK.messagebox.showwarning(
    title="Invalid Input",
    message="Please choose a color from given colors list.")


# draw a line
turtle_race.draw_endline()

# game_on = True
turtle_race.set_positions()
while turtle_race.game_on:
    turtle_race.move_turtles()


# print message who won
message = ''
winner_color = turtle_race.winner.pencolor()
if winner_color == user_bet:
    message = f'Congratulations!! The {winner_color} turtle has won.'
else:
    message = f'The winner is {winner_color} turtle. Try again next time.'

TK.messagebox.showinfo(title="Turtle Race", message=message)
s.mainloop()