import colorgram
colors = colorgram.extract( r"insert the path of image file here", 15)
#
rgb_colors = []
#
for color in colors:
#     # rgb_colors.append(color.rgb)
    rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))

# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random


# rgb_colors = [(231, 206, 85), (224, 150, 89), (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38), (171, 21, 16), (199, 65, 28), (185, 186, 27)]

t = Turtle()
turtle.colormode(255)
t.speed('fastest')
t.penup()
t.hideturtle()
t.setheading(225)
t.forward(300)
t.setheading(0)
for i in range(10):
    for j in range(10):
        t.dot(20, random.choice(rgb_colors))
        t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)


s = Screen()


s.exitonclick()
