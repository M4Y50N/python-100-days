from turtle import *
import random


# draw dashes
def draw_dashes():
    for _ in range(50):
        forward(10)
        penup()
        forward(10)
        pendown()


# draw shapes
def draw_shapes():
    shapes_colors = {"CornFlowerBlue": 3, "DarkOrchid": 4, "IndianRed": 5, "DeepSkyBlue": 6, "LightSeaGreen": 7,
                     "wheat": 8,
                     "SlateGray": 9, "SeaGreen": 10}

    for c, s in shapes_colors.items():
        for _ in range(s):
            pensize(10)
            color(c)
            forward(100)
            right(360 / s)
        s += 1


# random walk
def random_walk():
    image_size = 333
    # Setup Turtle
    pensize(10)  # Set size
    speed(10)  # Set the speed to maximum

    colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
              "wheat", "SlateGray", "SeaGreen"]

    directions = [0, 90, 180, 270]

    # Draw a colorful pattern
    for _ in range(image_size):
        direction = random.choice(directions)
        color(random.choice(colors))
        forward(20)
        setheading(direction)


def __main__():
    screen = Screen()

    # Call the functions bellow
    random_walk()

    # Hide the turtle and display the result
    hideturtle()
    screen.mainloop()


__main__()
