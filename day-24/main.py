from turtle import Screen
from Snake import Snake
from Food import Food
from Score import Score
import time

# Setup screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Initialize snake and food
snake = Snake()
food = Food()
score = Score()

# Listening to the keys to move the snake
screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")

# Run game
# game_is_on = True
while True:
    # Prevent/Allow screen to render
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.increment()
        snake.update_size()
        food.refresh()

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290
            or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        snake.reset()
        score.reset_score()

    # Detect collision with tail
    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()

# screen.exitonclick()
