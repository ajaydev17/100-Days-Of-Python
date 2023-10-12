from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=400)
screen.title("PING PONG")
screen.tracer(0)


paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_ycor = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_ycor)


def go_down():
    new_ycor = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_ycor)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_on = True
while game_on:
    screen.update()


screen.exitonclick()
