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
        self.cars = []

    def generate_cars(self):
        for i in range(random.randint(0, 10)):
            if i % 7 == 0 and i != 0:
                car = self.Car()
                car.shape("square")
                car.color(random.choice(COLORS))
                # car.shapesize(stretch_wid=1, stretch_len=2)
                car.goto(START_POSITION, random.randint(-240, 230))
                self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move()
            if car.xcor() < -290:
                car.hideturtle()
                car.clear()
                self.cars = self.cars[self.cars.index(car):]

    def increase_cars_speed(self):
        for car in self.cars:
            car.increase_speed()

    def collision(self, player):
        for car in self.cars:
            if player.distance(car) < 20:
                return True

    class Car(Turtle):
        def __init__(self):
            super().__init__()
            self.penup()
            self.speed = 5

        def move(self):
            self.goto(x=self.xcor() - self.speed, y=self.ycor())

        def increase_speed(self):
            self.speed += MOVE_INCREMENT
