from tkinter import *
from tkinter import messagebox
import random
import string
import json


# -------------- Search Credentials --------------
def search_credentials():
    try:
        with open("./data.json", mode="r") as saved_pass:
            data = json.load(saved_pass)
    except FileNotFoundError:
        messagebox.showwarning(title="Oops!", message="There's no data to search, please save a password first!")
    else:
        website = website_entry.get().capitalize()
        try:
            website_data = data[website]
            email = website_data["email"]
            password = website_data["password"]
        except KeyError:
            messagebox.showwarning(title="Oops!", message="Website doesn't exist!")
        else:
            messagebox.showinfo(title=website, message=f"email: {email}\n"
                                                       f"password: {password}")


# -------------- Password Generator --------------
letters = list(string.ascii_lowercase)
numbers = [str(i) for i in range(10)]
symbols = list(string.punctuation)


def generate_password():
    num_letters = random.randint(8, 10)
    num_numbers = random.randint(2, 4)
    num_symbols = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(num_letters)]
    password_list.append([random.choice(numbers) for _ in range(num_numbers)])
    password_list.append([random.choice(symbols) for _ in range(num_symbols)])

    password = []
    for i in password_list:
        if isinstance(i, list):
            password.extend(i)
        else:
            if isinstance(i, str):
                if random.randint(0, 1) == 1:
                    password.append(i.upper())
                else:
                    password.append(i)
            else:
                password.append(i)

    random.shuffle(password)
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(password))


# -------------- Save Password --------------
def save_pass():
    check_fields = {
        "website": website_entry.get().capitalize(),
        "email": email_user_entry.get(),
        "password": password_entry.get()
    }

    missing_fields = []
    for k, v in check_fields.items():
        if not v:
            missing_fields.append(k)

    if len(missing_fields):
        missing_fields_text = ''.join(
            (f + ", ") if i != len(missing_fields) - 2 else (f + " and ") if len(missing_fields) > 1 else f for i, f in
            enumerate(missing_fields))
        missing_fields_text = missing_fields_text.rstrip(", ")

        messagebox.showwarning(title="Missing Fields",
                               message=f"Try to fill the follow field(s) {missing_fields_text}.")
    else:
        website = check_fields["website"]
        email = check_fields["email"]
        password = check_fields["password"]

        new_pass_fields = {website: {
            "email": email,
            "password": password}}

        website_value = check_fields["website"]
        confirm = messagebox.askokcancel(title=website_value, message=f"These are the details entered: "
                                                                      f"\nEmail: {check_fields["email"]} "
                                                                      f"\nPassword: {check_fields["password"]} "
                                                                      f"\nIs it ok to save?")
        if confirm:
            try:
                with open("./data.json", mode="r") as saved_pass:
                    data = json.load(saved_pass)
            except FileNotFoundError:
                with open("./data.json", mode="w") as saved_pass:
                    json.dump(new_pass_fields, saved_pass, indent=4)
            else:
                data.update(new_pass_fields)
                with open("./data.json", mode="w") as saved_pass:
                    json.dump(data, saved_pass, indent=4)
            finally:
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
website_entry = Entry(width=33)
website_entry.focus()
website_entry.grid(row=1, column=1)
website_button = Button(text="Search", width=15, command=search_credentials)
website_button.grid(row=1, column=2)

email_user_entry = Entry(width=52)
email_user_entry.grid(row=2, column=1, columnspan=2)
email_user_label = Label(text="Email/Username:")
email_user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=33)
password_entry.grid(row=3, column=1)
generate_pass_button = Button(text="Generate Password", width=15, command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_pass)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
