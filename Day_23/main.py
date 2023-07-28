import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

#Create the player
player = Player()


#Create the car manager
car_manager = CarManager()
cars = car_manager.num_of_cars

#Create the score
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()


    #Check if player has reached the finish line
    if player.ycor() > 280:
        cars += 10
        player.reset_position()
        scoreboard.level_up()
        car_manager.create_cars(num_of_cars=cars)

screen.exitonclick()