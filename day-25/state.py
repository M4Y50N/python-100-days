from turtle import Turtle

class State(Turtle):
    def __init__(self, name, coord):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.name = name
        self.x = coord[0]
        self.y = coord[1]
        self.goto(self.x, self.y)
        self.write(arg=self.name)
