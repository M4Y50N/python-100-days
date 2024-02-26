from turtle import Turtle
import random


SPEED = 0.07


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.ball_speed = SPEED
        self.x_move = self.x_move = random.choice((-10, 10))
        self.y_move = None
        self.random_direction()

    def random_direction(self):
        self.y_move = random.choice((-10, -9, -8, -7, 7, 8, 9, 10))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_speed = SPEED
        self.bounce_x()
        self.random_direction()

    def increase_speed(self):
        self.ball_speed *= 0.77 if self.ball_speed >= 0.01 else 1

