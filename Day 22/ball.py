from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        new_xcor = self.xcor() + self.x
        new_ycor = self.ycor() + self.y
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.y = self.y * -1

    def bounce_x(self):
        self.x = self.x * -1
        self.move_speed = self.move_speed * 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

