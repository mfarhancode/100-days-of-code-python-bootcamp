import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

p = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(p.move, key='Up')
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(p) < 20:
            scoreboard.game_over()
            game_is_on = False

    # finish line

    if p.is_at_finish_line():
        p.reset_position()
        car_manager.level_up()
        scoreboard.level_up()



#
# c_list = []
#
# count = 0
#
# while game_is_on:
#     count += 1
#     time.sleep(0.1)
#     screen.update()
#
#
#     # finish line
#     if p.ycor() > 280:
#         p.reset_position()
#
#     # creating cars
#
#     # print(count)
#     if count == 6:
#         c = CarManager()
#         c_list.append(c)
#         count = 0
#
#     for car in c_list:
#         car.move()
#
#          # detecting collision with car
#         if p.distance(car) < 20:
#             game_is_on = False




screen.exitonclick()