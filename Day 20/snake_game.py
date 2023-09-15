from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake_position = [(0, 0), [-20, 0], [-40, 0]]
segments = []

for position in snake_position:
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(position)
    segments.append(new_turtle)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for index in range(len(segments) - 1, 0, -1):
        new_x = segments[index - 1].xcor()
        new_y = segments[index - 1].ycor()
        segments[index].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
