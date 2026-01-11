from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(snake.up, 'Up')
s.onkey(snake.down, 'Down')
s.onkey(snake.left, 'Left')
s.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        # print('nom nom nom')
        food.refresh()
        score.increase_score()
        snake.extend()

    # Detect collision with wall.
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     game_is_on = False
    #     score.game_over()

    # Detect collision with wall but not ending the game, move the snake's head to another side of screen
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.change_head_position()
    # game_is_on = False
    #     score.game_over()

    # if snake.head.xcor() > 280:
        # snake.change_head_position()
        # x, y = snake.head.xcor(), snake.head.ycor()
        # snake.head.goto(-x, y)

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


s.exitonclick()
