from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

color = ["red", "green", "blue", "yellow", "pink", "orange"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? choose a color.")
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You have won!!, {winning_turtle} turtle has won the race!!")
            else:
                print(f"You have lost!!, {winning_turtle} turtle has won the race!!")

        step = random.randint(0, 10)
        turtle.forward(step)


screen.exitonclick()
