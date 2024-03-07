from tkinter import *
import pandas
import random

FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"


# Random Words
def random_word():
    data = pandas.read_csv("./data/french_words.csv")

    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=random.choice(data["French"]))


# UI
window = Tk()
window.title("")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=544, highlightthickness=0)
canvas.config(bg=BACKGROUND_COLOR)
canvas.grid(row=0, column=0, columnspan=2)

card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 270, image=card_front)

title = canvas.create_text(400, 180, text="Title", font=(FONT_NAME, 24, "italic"))
word = canvas.create_text(400, 265, text="Word", font=(FONT_NAME, 36, "bold"))

right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
right_button = Button(image=right, highlightthickness=0, cursor="hand2", command=random_word)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong, highlightthickness=0, cursor="hand2", command=random_word)
wrong_button.grid(row=1, column=0)

random_word()

window.mainloop()
