import turtle
import random
import Colours as c

t = turtle.Turtle()
t.penup()
turtle.colormode(255)
t.pensize(10)
t.speed(0)
t.hideturtle()
color = c.list_colors()

x = -200
y = -200

for _ in range(0, 10):
    t.setposition(x, y)
    for i in range(0, 10):
        t.dot(20, random.choice(color))
        t.forward(50)
    y += 50

screen = turtle.Screen()
screen.exitonclick()