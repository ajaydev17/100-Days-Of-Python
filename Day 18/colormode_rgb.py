import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.pensize(10)
timmy.speed('fast')

direction = [0, 90, 180, 270]


def random_colors():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


for _ in range(200):
    timmy.color(random_colors())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))

screen = turtle.Screen()
screen.exitonclick()
