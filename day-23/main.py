from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen.onkey(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Generate Cars
    car_manager.generate_cars()

    # Detect if player won
    if player.ycor() >= 280:
        player.reset_level()
        score.pass_level()
        car_manager.increase_cars_speed()

    # Detect collision with cars
    if car_manager.collision(player):
        score.game_over()
        game_is_on = False

    car_manager.move_cars()

screen.exitonclick()
