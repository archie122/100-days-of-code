from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) # turn off animation

# Create Paddle
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(paddle1.go_up, "Up")
screen.onkey(paddle1.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True
while game_is_on: # game loop, so that the contents are displayed on the screen
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Score
    if ball.xcor() > 340:
        ball.reset_position()
        score.add_left_score()
    if ball.xcor() < -340:
        ball.reset_position()
        score.add_right_score()




screen.exitonclick()
