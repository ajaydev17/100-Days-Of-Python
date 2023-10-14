from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 260)
        self.write(f"{self.left_score}", align="center", font=("Courier-Bold", 24, "normal"))
        self.goto(100, 260)
        self.write(f"{self.right_score}", align="center", font=("Courier-Bold", 24, "normal"))

    def update_right_score(self):
        self.right_score = self.right_score + 1
        self.update_score()

    def update_left_score(self):
        self.left_score = self.left_score + 1
        self.update_score()
