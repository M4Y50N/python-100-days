from turtle import Turtle


UP_RIGHT = 45
UP_LEFT = 135
DOWN_LEFT = 225
DOWN_RIGHT = 315


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")

    def move(self):
        self.goto(x=self.xcor() + 10, y=self.ycor() + 10)
