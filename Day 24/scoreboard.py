from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier-Bold", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score()
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_score()
        self.score = 0
        self.update_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over!!", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_board()

    @staticmethod
    def read_score():
        with open("score.txt", "r") as score:
            current_score = int(score.read())
        return current_score

    def write_score(self):
        with open("score.txt", "w") as score:
            score.write(f"{self.high_score}")
