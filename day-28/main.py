from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

checkmark = "✔"

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)

# Title
title = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW)
title.grid(row=0, column=1)

# Buttons
start_button = Button(text="Start")
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset")
reset_button.grid(row=2, column=2)

# Checkmark
check = Label(text=checkmark)
check.grid(row=3, column=1)

window.mainloop()
