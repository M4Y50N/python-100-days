from turtle import Screen
from Snake import Snake
import time

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize snake
snake = Snake()

# Listening to the keys to move the snake
screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

# Run game
game_is_on = True
while game_is_on:
    # Prevent/Allow screen to render
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
