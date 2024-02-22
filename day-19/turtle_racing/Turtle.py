from turtle import Turtle
from random import random


class TurtleClass(Turtle):
    def __init__(self, color, speed=0):
        super().__init__()
        self.color(color)
        self.speed = speed
        self.penup()
        self.shape("turtle")

    def random_walk(self):
        return random() * self.speed

    def turtle_walk(self):
        self.forward(self.random_walk())

