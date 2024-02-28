from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increment(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()

    # def game_over(self):
        # self.goto(0, 0)
        # self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        # self.goto(0, -20)
        # self.write("Press SPACE to play again", align=ALIGNMENT, font=FONT)
