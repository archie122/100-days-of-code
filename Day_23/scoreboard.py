from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-260, 260)
        self.level = 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level : {self.level}", move=False, align='left', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=FONT)