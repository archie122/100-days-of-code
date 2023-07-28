from turtle import Turtle

X_POS = 0
Y_POS = 240
ALIGNMENT = 'center'
FONT = ('Arial', 30, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score1 = 0
        self.score2 = 0
        self.color("white")
        self.goto(X_POS, Y_POS)
        self.write_score()

    def write_score(self):
        self.write(f"{self.score1} : {self.score2}", move=False, align=ALIGNMENT, font=FONT)

    def add_left_score(self):
        self.score1 += 1
        self.clear()
        self.goto(X_POS, Y_POS)
        self.write(f"{self.score1} : {self.score2}", move=False, align=ALIGNMENT, font=FONT)

    def add_right_score(self):
        self.score2 += 1
        self.clear()
        self.goto(X_POS, Y_POS)
        self.write(f"{self.score1} : {self.score2}", move=False, align=ALIGNMENT, font=FONT)
