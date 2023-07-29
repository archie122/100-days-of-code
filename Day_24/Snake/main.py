import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time
from score import Score_Board

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create Snake
snake = Snake()
food = Food()
score = Score_Board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move Snake forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Check if the snake had gotten food 
    if snake.head.distance(food) < 15:
        snake.add_segment()
        score.add_score()
        food.new_postion()
    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # Detect if the snake collides with its
    for i in snake.list_snake[1:]:
        if snake.head.distance(i) < 10:
            score.reset()
            snake.reset()
screen.exitonclick()
