from turtle import Turtle, Screen

# creating a turtle object and screen object
timmy = Turtle()
my_screen = Screen()

# access the object attributes
print(my_screen.canvheight)

# access the object methods
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen.exitonclick()
