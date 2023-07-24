from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)

user_choice = screen.textinput(title="What Colour is going to win?", prompt="Choose a color: ").lower()
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]

if user_choice:
    is_game_on = True

# t1 = Turtle("turtle")
# t1.penup()
# t1.color("red")
# t1.goto(x=-230, y=-70)
#
# t2 = Turtle("turtle")
# t2.penup()
# t2.color("orange")
# t2.goto(x=-230, y=-40)
#
# t3 = Turtle("turtle")
# t3.penup()
# t3.color("yellow")
# t3.goto(x=-230, y=-10)
#
# t4 = Turtle("turtle")
# t4.penup()
# t4.color("green")
# t4.goto(x=-230, y=20)
#
# t5 = Turtle("turtle")
# t5.penup()
# t5.color("blue")
# t5.goto(x=-230, y=50)
#
# t6 = Turtle("turtle")
# t6.penup()
# t6.color("purple")
# t6.goto(x=-230, y=80)

list_of_turtles = []

for i in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(color_list[i])
    new_turtle.goto(x=-230, y=y_pos[i])
    list_of_turtles.append(new_turtle)

print(list_of_turtles)

while is_game_on:
    for turtle in list_of_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You won! The {winning_color} turtle is the winner!")
            else :
                print(f"You lost! The {winning_color} turtle is the winner!")
        random.choice(list_of_turtles).forward(random.randint(0, 10))


screen.exitonclick()