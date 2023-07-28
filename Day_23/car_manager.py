from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEEDS = [1, 1.5 , 2, 2.5, 3, 3.5]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.num_of_cars = 20
        self.penup()
        self.create_cars()

    def create_cars(self, num_of_cars=20):
        for i in range(num_of_cars):
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(random.randint(-250, 2000), random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self, speed=0):
        for car in self.all_cars:
            car.backward(random.randint(0, MOVE_INCREMENT * SPEEDS[speed]))