from Turtle import TurtleClass as Turtle
from turtle import Screen


def game():
    # Setup screen
    screen = Screen()
    screen.colormode(255)
    screen.setup(width=500, height=400)
    user_bet = screen.textinput("Make your bet", "Which turtle will win, red, blue, green or pink?")
    turtles_colors = ["red", "blue", "green", "pink"]
    y_positions = [60, 30, 0, -30]
    turtles = []

    # Setup turtles
    for i, tc in enumerate(turtles_colors):
        new_turtle = Turtle(tc, 10)
        new_turtle.goto(x=-230, y=y_positions[i])
        turtles.append(new_turtle)

    # Start racing
    def start_racing():
        # Race status
        is_race_on = True
        while is_race_on:
            for racing_turtle in turtles:
                racing_turtle.turtle_walk()
                if racing_turtle.xcor() > 220:
                    is_race_on = False
                    break

        winner = max(turtles, key=lambda t: t.xcor())
        winner_color = winner.fillcolor()

        print(f'Congratulations {winner_color.capitalize()} turtle wins!!!' if user_bet == winner_color
              else f'You lose {winner_color.capitalize()} turtle wins!!!')

    screen.listen()
    screen.onkey(key="space", fun=start_racing)

    screen.exitonclick()


if __name__ == "__main__":
    game()
