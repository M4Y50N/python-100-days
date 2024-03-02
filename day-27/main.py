from tkinter import *


def convert_to_km():
    res_text.config(text=round(1.6 * float(text_input.get()), 2))


FONT = ("Arial", 12, "normal")

window = Tk()
window.title("Miles to KM Converter")
window.config(padx=20, pady=20)

# Label
miles = Label(text="Miles", font=FONT)
miles.grid(column=3, row=1)

# Entry
text_input = Entry()
text_input.config(width=10)
text_input.grid(column=2, row=1)

# Button
calc_button = Button(text="Calculate", command=convert_to_km)
calc_button.grid(column=2, row=3)

# KM Label
is_equal = Label(text="is equal to ", font=FONT)
is_equal.grid(column=1, row=2)
res_text = Label(font=FONT)
res_text.grid(column=2, row=2)
km = Label(text="Km", font=FONT)
km.grid(column=3, row=2)

window.mainloop()
