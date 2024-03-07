from tkinter import *

FONT_NAME = "Ariel"
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=1000, height=670)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)

card_front = PhotoImage(file="./images/card_front.png")
canvas.create_image(500, 270, image=card_front)

title = canvas.create_text(500, 180, text="Title", font=(FONT_NAME, 24, "italic"))
word = canvas.create_text(500, 265, text="Word", font=(FONT_NAME, 36, "bold"))

right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")
canvas.create_image(700, 600, image=right)
canvas.create_image(300, 600, image=wrong)

window.mainloop()
