from turtle import Turtle


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.size = 3
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for _ in range(self.size):
            snake = Turtle("square")
            snake.penup()
            snake.color("white")
            self.body.append(snake)

        [part.goto(i * -20, 0) for i, part in enumerate(self.body)]

    def update_size(self):
        ...

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            next_x = self.body[seg_num - 1].xcor()
            next_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(x=next_x, y=next_y)

        # Snake's head
        self.head.forward(20)

    def move_up(self):
        if self.head.heading() != 270:
            self.head.seth(90)

    def move_down(self):
        if self.head.heading() != 90:
            self.head.seth(270)

    def move_left(self):
        if self.head.heading() != 0:
            self.head.seth(180)

    def move_right(self):
        if self.head.heading() != 180:
            self.head.seth(0)
