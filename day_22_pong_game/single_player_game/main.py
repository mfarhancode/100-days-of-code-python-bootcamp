from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddle = Paddle((0, -280))
print(paddle.ycor())

ball = Ball()

screen.listen()
screen.onkeypress(paddle.go_left, 'Left')
screen.onkeypress(paddle.go_right, 'Right')


score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280:
        ball.bounce_y()
    
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # Detect collision with paddle
    # if (ball.distance(paddle) < 50 and ball.ycor() < -260):
    if (ball.y_move < 0 and ball.ycor() < -260 and abs(ball.xcor() - paddle.xcor()) < 50):
        ball.bounce_y()
        ball.speed_up()
        score.point()

    # Detect  paddle misses
    if (ball.ycor() < -280):
        score.game_over()
        game_is_on = False
        # pass


screen.exitonclick()