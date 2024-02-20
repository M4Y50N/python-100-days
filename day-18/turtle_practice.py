from turtle import *
import random


# draw dashes
def draw_dashes():
    for _ in range(50):
        forward(10)
        penup()
        forward(10)
        pendown()


# Random Colors
def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


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
    pensize(15)  # Set size


    # colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
    #     #           "wheat", "SlateGray", "SeaGreen"]

    directions = [0, 90, 180, 270]

    # Draw a colorful pattern
    for _ in range(image_size):
        direction = random.choice(directions)
        color((random_colors()))
        forward(30)
        setheading(direction)


# Spirograph
def spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        color(random_colors())
        circle(100)
        current_heading = heading()
        setheading(current_heading + size_of_gap)


def __main__():
    screen = Screen()

    speed("fastest")  # Set the speed to maximum

    # Change colormode
    screen.colormode(255)

    # Call the functions bellow
    spirograph(5)

    # Hide the turtle and display the result
    hideturtle()
    screen.mainloop()


__main__()
