from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.list_snake = []
        self.create_snake()
        self.head = self.list_snake[0]

    def create_snake(self):
        for i in START_POSITION:
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            snake.goto(i)
            self.list_snake.append(snake)

    def move(self):
        for seg_num in range(len(self.list_snake) - 1, 0, -1):
            new_x = self.list_snake[seg_num - 1].xcor()
            new_y = self.list_snake[seg_num - 1].ycor()
            self.list_snake[seg_num].goto(new_x, new_y)
        self.list_snake[0].forward(MOVE_DISTANCE)

    def reset(self):
        for seg in self.list_snake:
            seg.goto(1000, 1000)

        self.list_snake.clear()
        self.create_snake()
        self.head = self.list_snake[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.list_snake[-1].position())
        self.list_snake.append(new_segment)
