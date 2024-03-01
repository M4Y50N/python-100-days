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
all_states = data_states["state"].to_list()


guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 Guess the State",
                                    "What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv("missing_states.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state = data_states[data_states["state"] == answer_state]
        State(answer_state, (int(state.x), int(state.y)))

# screen.mainloop()
