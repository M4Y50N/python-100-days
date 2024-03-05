from tkinter import *
from tkinter import messagebox


# -------------- Save Password --------------
def save_pass():
    new_pass_dict = {
        "website": website_entry.get(),
        "email": email_user_entry.get(),
        "password": password_entry.get()
    }

    confirm = messagebox.askokcancel(title=new_pass_dict["website"], message=f"These are the details entered: "
                                                                 f"\nEmail: {new_pass_dict["email"]} "
                                                                 f"\nPassword: {new_pass_dict["password"]} "
                                                                 f"\nIs it ok to save?")
    if confirm:
        with open("./data.txt", mode="a") as saved_pass:
            saved_pass.write(f"{new_pass_dict["website"]} | {new_pass_dict["email"]} | {new_pass_dict["password"]}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -------------- UI --------------
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Form
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_user_entry = Entry(width=52)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
