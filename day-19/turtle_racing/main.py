from Turtle import TurtleClass as Turtle
from turtle import Screen


def game():
    # Setup screen
    screen = Screen()
    screen.colormode(255)
    screen.setup(width=500, height=400)
    users_turtle = screen.textinput("Turtle", "Choice a color between red, blue, green or pink")

    # Setup turtles
    timmy = Turtle("red", 10)
    tommy = Turtle("blue", 10)
    bonny = Turtle("green", 10)
    billy = Turtle("pink", 10)

    timmy.goto(-230, 0)
    tommy.goto(-230, 50)
    bonny.goto(-230, 100)
    billy.goto(-230, -50)

    # Start racing
    def start_racing():
        while timmy.xcor() < 210 and tommy.xcor() < 210 and bonny.xcor() < 210 and billy.xcor() < 210:
            timmy.turtle_walk()
            tommy.turtle_walk()
            bonny.turtle_walk()
            billy.turtle_walk()

        turtles = [timmy, tommy, bonny, billy]
        winner = max(turtles, key=lambda t: t.xcor())
        winner_color = winner.fillcolor()

        print(f'Congratulations {winner_color.capitalize()} turtle wins!!!' if users_turtle == winner_color
              else f'You lose {winner_color.capitalize()} turtle wins!!!')

    screen.listen()
    screen.onkey(key="space", fun=start_racing)

    screen.exitonclick()


if __name__ == "__main__":
    game()
