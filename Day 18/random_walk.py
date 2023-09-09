from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.pensize(10)
timmy.speed('fast')

colors = ["green", "crimson", "magenta", "indigo", "light salmon", "maroon", "medium violet red", "olive drab"]
direction = [0, 90, 180, 270]

for _ in range(200):
    timmy.color(random.choice(colors))
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
