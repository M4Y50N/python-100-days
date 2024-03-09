import time
from tkinter import *
import pandas
import random

FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
current_card = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Random Words
def random_word():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    guess_word, answer_word = current_card["French"], current_card["English"]
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=guess_word, fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    guess_word, answer_word = current_card["French"], current_card["English"]
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=answer_word, fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data_to_learn = pandas.DataFrame(to_learn)
    data_to_learn.to_csv("./data/words_to_learn.csv", index=False)
    random_word()


# UI
window = Tk()
window.title("")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=544, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 270, image=card_front)

title = canvas.create_text(400, 180, text="Title", font=(FONT_NAME, 24, "italic"))
word = canvas.create_text(400, 265, text="Word", font=(FONT_NAME, 36, "bold"))

right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right, highlightthickness=0, cursor="hand2", command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong, highlightthickness=0, cursor="hand2", command=random_word)
wrong_button.grid(row=1, column=0)

random_word()

window.mainloop()
