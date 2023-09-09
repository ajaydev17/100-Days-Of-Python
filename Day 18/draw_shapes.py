from turtle import Turtle, Screen
import random

timmy = Turtle()

colors = ["green", "crimson", "magenta", "indigo", "light salmon", "maroon", "medium violet red", "olive drab"]


def draw_shape(number_of_sides):
    angle = 360 / number_of_sides
    for _ in range(number_of_sides):
        timmy.forward(100)
        timmy.right(angle)


for side in range(3, 10):
    timmy.color(random.choice(colors))
    draw_shape(side)

screen = Screen()
screen.exitonclick()
