from tkinter import *


def convert_to_km():
    res_text.config(text=round(MILES * float(text_input.get()), 2))


MILES = 1.609
FONT = ("Arial", 12, "normal")

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# Label
miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

# Entry
text_input = Entry()
text_input.config(width=10)
text_input.grid(column=1, row=0)

# Button
calc_button = Button(text="Calculate", command=convert_to_km)
calc_button.grid(column=1, row=2)

# KM Label
is_equal = Label(text="is equal to ", font=FONT)
is_equal.grid(column=0, row=1)
res_text = Label(text=0, font=FONT)
res_text.grid(column=1, row=1)
km = Label(text="Km", font=FONT)
km.grid(column=2, row=1)

window.mainloop()
