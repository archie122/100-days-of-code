import turtle as t
import random


turtle = t.Turtle()
turtle.pensize(5)
turtle.speed(0)
color = ["IndianRed2", "PaleVioletRed", "MediumSeaGreen", "Red", "MediumOrchid", "DeepSkyBlue", "Cyan", "LightBlue",
    "LightGreen", "LightSalmon", "Yellow"]

for _ in range(100):
    turtle.color(random.choice(color))
    turtle.circle(100)
    turtle.right(9)



screen = t.Screen()
screen.exitonclick()