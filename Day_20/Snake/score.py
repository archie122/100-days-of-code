from turtle import Turtle

X_POS = 0
Y_POS = 240
ALIGNMENT = 'center'
FONT = ('Arial', 30, 'normal')

class Score_Board (Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(X_POS, Y_POS)
        self.write_score()

    def write_score(self):
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.clear()
        self.score += 1
        self.goto(X_POS, Y_POS)
        self.write(f"Score : {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(X_POS, X_POS)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)