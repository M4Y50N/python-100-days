from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball
from turtle import Turtle
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))

ball = Ball()

score_1 = Score((120, 220))
score_2 = Score((-120, 220))

screen.listen()
screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")

screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(paddle_1) < 50 and ball.xcor() > 330 or ball.distance(paddle_2) < 50 and ball.xcor() < -330:
        ball.bounce_x()

        paddle_1.increase_speed()
        paddle_2.increase_speed()

    # Detect if paddle misses the ball
    # R Paddle
    if ball.xcor() > 380:
        ball.reset_ball()
        score_2.increment()

    # L Paddle
    if ball.xcor() < -380:
        ball.reset_ball()
        score_1.increment()

screen.exitonclick()
