from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
