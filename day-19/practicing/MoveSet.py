from turtle import Turtle


class MoveSet(Turtle):
    def __init__(self):
        super().__init__()

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

    def move_clockwise(self):
        self.right(10)

    def move_anticlockwise(self):
        self.left(10)

    def clear_screen(self):
        self.clear()
        self.penup()
        self.home()
        self.pendown()

