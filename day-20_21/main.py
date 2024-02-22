from turtle import Screen
from Snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")


game_is_on = True
while game_is_on:
    # Prevent/Allow screen to render
    screen.update()
    time.sleep(0.1)

    if snake.size < 10:
        snake.size += 1
        snake.update_size()

    snake.move()

screen.exitonclick()
