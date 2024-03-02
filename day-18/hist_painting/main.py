import turtle
import random

# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.r
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)


color_list = [(226, 226, 236), (58, 58, 148), (224, 224, 109), (134, 134, 58), (223, 223, 62), (196, 196, 171),
              (234, 234, 204), (224, 224, 230), (141, 141, 204), (139, 139, 105), (209, 209, 69), (188, 188, 120),
              (68, 68, 90), (237, 237, 233), (134, 134, 136), (133, 133, 74), (63, 63, 92), (48, 48, 194),
              (183, 183, 201), (214, 214, 191), (19, 19, 93), (21, 21, 113), (112, 112, 149), (229, 229, 165),
              (172, 172, 182), (158, 158, 215), (69, 69, 47), (108, 108, 60), (53, 53, 65), (72, 72, 53)]


def hirst_painting(number_of_dots_per_row, colors_list):
    t = turtle.Turtle()
    screen = turtle.Screen()

    screen.colormode(255)

    t.hideturtle()
    t.speed("fastest")
    t.penup()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)
    for _ in range(number_of_dots_per_row):
        current_pos = t.pos()
        for _ in range(number_of_dots_per_row):
            t.dot(20, random.choice(color_list))
            t.forward(50)
        t.setpos(current_pos[0], current_pos[1] + 50)

    screen.exitonclick()

hirst_painting(2, color_list)
