from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(pos[0], pos[1])
        self.move_y = 20

    def go_up(self):
        new_y = self.ycor() + self.move_y
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.move_y
        self.goto(self.xcor(), new_y)

    def increase_speed(self):
        self.move_y *= 1.099 if self.move_y < 45 else 1  # Maximum 46.77

