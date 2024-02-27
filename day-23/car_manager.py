from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_POSITION = 290
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def generate_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(START_POSITION, random.randint(-240, 240))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.speed)
            if car.xcor() < -290:
                car.hideturtle()
                car.clear()
                self.cars = self.cars[self.cars.index(car):]

    def increase_cars_speed(self):
        self.speed += MOVE_INCREMENT

    def collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True
