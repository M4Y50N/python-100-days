import pandas
import turtle
import time

from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data_states = pandas.read_csv("./50_states.csv")
states = data_states["state"].to_list()

screen.tracer(0)

guessed_states = []
while len(guessed_states) < 50:
    time.sleep(.5)
    screen.update()
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guess the State", "What's another state's name?").capitalize()

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = data_states[data_states["state"] == answer_state]
        State(answer_state, (state.x.to_list()[0], state.y.to_list()[0]))

screen.mainloop()
