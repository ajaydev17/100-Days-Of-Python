import turtle


timmy = turtle.Turtle()
screen = turtle.Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_left():
    current_heading = timmy.heading()
    timmy.setheading(current_heading + 10)


def move_right():
    current_heading = timmy.heading()
    timmy.setheading(current_heading - 10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick()
