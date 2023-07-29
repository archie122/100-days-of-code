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
        self.high_score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color("white")
        self.goto(X_POS, Y_POS)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.write_score()