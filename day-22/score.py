from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 36, "bold")


class Score(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(pos[0], pos[1])
        self.write(self.score, align=ALIGNMENT, font=FONT)
        self.hideturtle()


    def increment(self):
        self.score += 1
        self.clear()
        self.write(self.score, align=ALIGNMENT, font=FONT)
