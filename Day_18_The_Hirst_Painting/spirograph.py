import random
from turtle import Turtle, Screen
from random import choice

tim = Turtle()

tim.colormode(255)
def random_color():
    r = random.randint(2,255)
    g = random.randint(2, 255)
    b = random.randint(2, 255)
    return (r,g,b)

tim.speed('fastest')
def draw_spirograph(size_of_gap):
    for i in range(360 // size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(4)













screen = Screen()
screen.exitonclick()

# tuple = (1,2,3)
# a = list(tuple)
# # tuple[0] = 5
# print(a)