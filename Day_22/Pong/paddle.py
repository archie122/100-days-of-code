from turtle import Turtle

class Paddle(Turtle):
    '''
    When working with inheritance, it is important to realize
    that the self keyword is used to refer to the class itself.
    In this case, the self keyword refers to the Turtle class,
    thus making the code more readable.
    '''

    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.speed(0)

    def go_up(self):
        y = self.ycor()
        if y <= 240:
            y += 20
        self.sety(y)

    def go_down(self):
        y = self.ycor()
        if y >= -240:
            y -= 20
        self.sety(y)