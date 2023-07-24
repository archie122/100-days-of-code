import turtle
from turtle import Turtle, Screen

t = Turtle()
turtle.colormode(255)
screen = Screen()
t.speed("fastest")
t.pensize(5)
t.color((129, 190, 131))


def move_forwards():
    t.forward(10)


def move_backwards():
    t.backward(10)


def turn_right():
    t.right(10)


def turn_left():
    t.left(10)


def clear():
    t.home()
    t.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)  # Example of a higer order function
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
