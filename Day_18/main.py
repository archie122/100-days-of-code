import turtle as t
import random

# from turtle import * (This is very bad practice)
# import turtle (If you are only importing a single module, just import the whole thing)
# import turtle as t (This way you are able to both import the corresponding module and name in one line)

timmy = t.Turtle()
t.colormode(255)
timmy.pensize(10)
timmy.speed(0)
# color = ["IndianRed2", "PaleVioletRed", "MediumSeaGreen", "Red", "MediumOrchid", "DeepSkyBlue", "Cyan", "LightBlue",
#          "LightGreen", "LightSalmon", "Yellow"]


# for _ in range(4): Drawing a square
#     t.forward(100)
#     t.right(90)

# for _ in range(15):
#     t.forward(10)
#     t.penup()
#     t.forward(10)
#     t.pendown()

# num_sides = 3
#
# for _ in range(3, 11):
#     for _ in range(num_sides):
#         angle = 360 / num_sides
#         t.forward(100)
#         t.right(angle)
#     num_sides += 1

def random_side():
    return random.randint(0, 4)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    x = (r, g, b)
    return x

for _ in range(200):
    timmy.pencolor(random_color())
    timmy.forward(20)
    timmy.right(random_side() * 90)
    timmy.forward(20)
    timmy.left(random_side() * 90)

screen = t.Screen()
screen.exitonclick()
