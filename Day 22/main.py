from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PING PONG")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # when ping ball hits the upper and lower walls
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # detect the collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when ball goes out of the bound (right paddle)
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.update_left_score()

    # detect when ball goes out of the bound (left paddle)
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.update_right_score()


screen.exitonclick()
