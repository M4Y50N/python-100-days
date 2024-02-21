from MoveSet import MoveSet
from turtle import Screen

move_set = MoveSet()
listener = Screen()

listener.listen()
listener.onkey(move_set.move_forward, "w")
listener.onkey(move_set.move_backward, "s")
listener.onkey(move_set.move_clockwise, "d")
listener.onkey(move_set.move_anticlockwise, "a")
listener.onkey(move_set.clear_screen, "c")
listener.exitonclick()
