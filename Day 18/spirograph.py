import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)
timmy.speed('fastest')


def random_colors():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_colors())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)


draw_circle(5)
screen = turtle.Screen()
screen.exitonclick()
