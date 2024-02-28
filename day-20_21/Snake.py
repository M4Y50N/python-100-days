from turtle import Turtle

COLOR = "white"

STEP = 20

RIGHT = 0
LEFT = 180
UP = 90
DOWN = 270


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.size = 3
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for i in range(self.size):
            self.add_segment((i * -20, 0))

    def add_segment(self, pos):
        new_segment = Turtle("square")
        new_segment.color(COLOR)
        new_segment.penup()
        new_segment.goto(pos)
        self.body.append(new_segment)

    def update_size(self):
        self.add_segment(self.body[-1].position())

    def reset(self):
        [seg.goto(1000, 1000) for seg in self.body]
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def move(self):
        for seg_num in range(len(self.body) - 1, 0, -1):
            next_x = self.body[seg_num - 1].xcor()
            next_y = self.body[seg_num - 1].ycor()
            self.body[seg_num].goto(x=next_x, y=next_y)

        # Snake's head
        self.head.forward(STEP)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

